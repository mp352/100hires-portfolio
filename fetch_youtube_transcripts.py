#!/usr/bin/env python3
"""Fetch YouTube transcripts and save them as .txt files."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from youtube_transcript_api import (
    AgeRestricted,
    InvalidVideoId,
    IpBlocked,
    NoTranscriptFound,
    PoTokenRequired,
    RequestBlocked,
    TranscriptsDisabled,
    VideoUnavailable,
    VideoUnplayable,
    YouTubeRequestFailed,
    YouTubeTranscriptApi,
)

OUTPUT_DIR = Path(__file__).resolve().parent / "research" / "youtube-transcripts"
DEFAULT_LANGUAGES = ("en",)


@dataclass(frozen=True)
class VideoTarget:
    """A YouTube video ID and the output filename to write."""

    video_id: str
    filename: str


# Add video IDs here. Use the ID from the URL (e.g. watch?v=abc123 -> abc123).
VIDEO_LIST: list[VideoTarget] = [
    VideoTarget(
        video_id="h2j0gFz9RH4",
        filename="nick_abraham_infrastructure.txt",
    ),
    VideoTarget(
        video_id="ta2G6yihCSs",
        filename="alex_berman_templates.txt",
    ),
]


def transcript_to_text(transcript) -> str:
    """Join transcript snippets into plain text, one line per snippet."""
    return "\n".join(snippet.text.strip() for snippet in transcript if snippet.text.strip())


def fetch_transcript(
    api: YouTubeTranscriptApi,
    video_id: str,
    languages: Iterable[str] = DEFAULT_LANGUAGES,
) -> str:
    transcript = api.fetch(video_id, languages=list(languages))
    text = transcript_to_text(transcript)
    if not text:
        raise ValueError("transcript fetched but contained no text")
    return text


def save_transcript(filename: str, text: str) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / filename
    output_path.write_text(text, encoding="utf-8")
    return output_path


def describe_error(exc: Exception) -> str:
    if isinstance(exc, TranscriptsDisabled):
        return "transcripts are disabled for this video"
    if isinstance(exc, NoTranscriptFound):
        return "no transcript found for the requested language(s)"
    if isinstance(exc, VideoUnavailable):
        return "video is unavailable"
    if isinstance(exc, VideoUnplayable):
        return "video is unplayable"
    if isinstance(exc, AgeRestricted):
        return "video is age-restricted"
    if isinstance(exc, InvalidVideoId):
        return "invalid video ID"
    if isinstance(exc, (RequestBlocked, IpBlocked)):
        return "request blocked by YouTube (rate limit or IP block)"
    if isinstance(exc, PoTokenRequired):
        return "YouTube requires additional authentication for this video"
    if isinstance(exc, YouTubeRequestFailed):
        return f"YouTube request failed: {exc}"
    return str(exc)


def process_video(
    api: YouTubeTranscriptApi,
    video_id: str,
    filename: str,
    languages: Iterable[str],
) -> bool:
    try:
        text = fetch_transcript(api, video_id, languages=languages)
        output_path = save_transcript(filename, text)
        print(f"[OK] {video_id} -> {output_path} ({len(text)} characters)")
        return True
    except (
        TranscriptsDisabled,
        NoTranscriptFound,
        VideoUnavailable,
        VideoUnplayable,
        AgeRestricted,
        InvalidVideoId,
        RequestBlocked,
        IpBlocked,
        PoTokenRequired,
        YouTubeRequestFailed,
    ) as exc:
        print(f"[ERROR] {video_id}: {describe_error(exc)}", file=sys.stderr)
        return False
    except Exception as exc:
        print(f"[ERROR] {video_id}: unexpected error - {exc}", file=sys.stderr)
        return False


def build_targets(args: argparse.Namespace) -> list[VideoTarget]:
    if args.video_ids:
        return [
            VideoTarget(video_id=video_id, filename=f"{video_id}.txt")
            for video_id in args.video_ids
        ]
    return VIDEO_LIST


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch YouTube transcripts and save them as .txt files.",
    )
    parser.add_argument(
        "video_ids",
        nargs="*",
        help="Optional video IDs. When provided, overrides VIDEO_LIST and saves as <video_id>.txt.",
    )
    parser.add_argument(
        "--languages",
        nargs="+",
        default=list(DEFAULT_LANGUAGES),
        help="Preferred transcript languages, in priority order (default: en).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    targets = build_targets(args)

    if not targets:
        print("No videos to process. Add entries to VIDEO_LIST or pass video IDs.", file=sys.stderr)
        return 1

    api = YouTubeTranscriptApi()
    successes = 0

    for target in targets:
        if process_video(api, target.video_id, target.filename, args.languages):
            successes += 1

    failures = len(targets) - successes
    print(f"\nDone: {successes} saved, {failures} failed.")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
