"""
Mock API responses for testing Knowledge OS.

This module provides mock data that simulates YouTube API responses,
transcript API responses, and other external dependencies.
"""

from typing import Dict, List, Any


# ============================================================================
# YouTube API Mock Responses
# ============================================================================

MOCK_YOUTUBE_VIDEO_INFO = {
    "id": "dQw4w9WgXcQ",
    "title": "How to Build a Successful Startup",
    "channel": "Startup Channel",
    "channel_id": "UC123456",
    "duration": 600,
    "view_count": 50000,
    "like_count": 2500,
    "upload_date": "20240115",
    "tags": ["startup", "business", "entrepreneurship"],
    "thumbnail": "https://example.com/thumbnail.jpg",
    "description": "Learn how to build a successful startup from scratch.",
    "categories": ["Education"],
    "availability": "public"
}


MOCK_YOUTUBE_SHORT_URL = {
    "id": "abc123xyz",
    "title": "Short URL Video",
    "channel": "Test Channel",
    "duration": 180,
    "view_count": 1000,
    "upload_date": "20240201",
    "tags": ["test"],
    "thumbnail": "https://example.com/test.jpg"
}


MOCK_YOUTUBE_EMBED_URL = {
    "id": "embed123",
    "title": "Embed URL Video",
    "channel": "Embed Channel",
    "duration": 300,
    "view_count": 500,
    "upload_date": "20240215",
    "tags": ["embed"],
    "thumbnail": "https://example.com/embed.jpg"
}


# ============================================================================
# Transcript API Mock Responses
# ============================================================================

MOCK_TRANSCRIPT_DATA = [
    {"text": "Welcome to this video about building startups.", "start": 0.0, "duration": 5.2},
    {"text": "Today I'll share the key lessons from my entrepreneurial journey.", "start": 5.2, "duration": 8.4},
    {"text": "First, let's talk about finding the right problem to solve.", "start": 13.6, "duration": 6.8},
    {"text": "The best startups solve a real pain point for their customers.", "start": 20.4, "duration": 7.2},
    {"text": "Second, focus on building a minimum viable product quickly.", "start": 27.6, "duration": 9.1},
    {"text": "Don't try to build the perfect product from day one.", "start": 36.7, "duration": 5.9},
    {"text": "Third, get your first paying customers as soon as possible.", "start": 42.6, "duration": 8.3},
    {"text": "Revenue validates that people actually want what you're building.", "start": 50.9, "duration": 7.5},
    {"text": "In conclusion, focus on solving real problems and iterate quickly.", "start": 58.4, "duration": 6.1}
]


MOCK_TRANSCRIPT_TEXT = (
    "Welcome to this video about building startups. "
    "Today I'll share the key lessons from my entrepreneurial journey. "
    "First, let's talk about finding the right problem to solve. "
    "The best startups solve a real pain point for their customers. "
    "Second, focus on building a minimum viable product quickly. "
    "Don't try to build the perfect product from day one. "
    "Third, get your first paying customers as soon as possible. "
    "Revenue validates that people actually want what you're building. "
    "In conclusion, focus on solving real problems and iterate quickly."
)


# ============================================================================
# Profile Templates (Expected Output Formats)
# ============================================================================

STARTER_STORY_PROFILE_TEMPLATE = {
    "sections": [
        "Executive Summary",
        "Product",
        "Tech Stack",
        "Distribution",
        "Key Frameworks",
        "Metrics"
    ],
    "required_sections": ["Executive Summary", "Product", "Tech Stack"]
}


AI_LEADERS_PROFILE_TEMPLATE = {
    "sections": [
        "AI Thesis",
        "Mental Models",
        "Contrarian Views",
        "What They're Building"
    ],
    "required_sections": ["AI Thesis", "Mental Models"]
}


FOUNDERS_PROFILE_TEMPLATE = {
    "sections": [
        "Key Lessons",
        "Notable Quotes",
        "Journey",
        "Books"
    ],
    "required_sections": ["Books", "Key Lessons"]
}


MY_FIRST_MILLION_PROFILE_TEMPLATE = {
    "sections": [
        "Key Insights",
        "Lessons",
        "Resources"
    ],
    "required_sections": ["Key Insights"]
}


AI_ENGINEERING_PROFILE_TEMPLATE = {
    "sections": [
        "Core Framework",
        "Step-by-Step Implementation",
        "Tools",
        "Books"
    ],
    "required_sections": ["Core Framework", "Step-by-Step Implementation"]
}


INNER_WORK_PROFILE_TEMPLATE = {
    "sections": [
        "Core Wisdom",
        "Key Principles",
        "Practical Application",
        "Quotes"
    ],
    "required_sections": ["Core Wisdom", "Key Principles"]
}


# ============================================================================
# Sample Markdown Files
# ============================================================================

SAMPLE_RAW_TRANSCRIPT = """---
video_id: dQw4w9WgXcQ
title: "How to Build a Successful Startup"
channel: "Startup Channel"
duration: 600
view_count: 50000
upload_date: 20240115
tags: ["startup", "business", "entrepreneurship"]
thumbnail: https://example.com/thumbnail.jpg
---

Welcome to this video about building startups.
Today I'll share the key lessons from my entrepreneurial journey.
First, let's talk about finding the right problem to solve.
The best startups solve a real pain point for their customers.
Second, focus on building a minimum viable product quickly.
Don't try to build the perfect product from day one.
Third, get your first paying customers as soon as possible.
Revenue validates that people actually want what you're building.
In conclusion, focus on solving real problems and iterate quickly.
"""


SAMPLE_PROCESSED_PROFILE = """# Executive Summary

This startup founder built a $10M ARR business by focusing on product-led growth and customer validation.

## Product

A B2B SaaS platform that helps small businesses manage their customer relationships.

## Tech Stack

- Frontend: React + TypeScript
- Backend: Python (FastAPI)
- Database: PostgreSQL
- Hosting: AWS (EC2, RDS)
- CI/CD: GitHub Actions

## Distribution

- Content marketing (blog, YouTube)
- LinkedIn outreach
- Product hunting
- Word of mouth

## Key Frameworks

### 1. The MVP Framework
Build the smallest thing that solves the core problem. Launch in 2 weeks.

### 2. The Seed Customer Method
Find 10 customers who represent your ideal ICP before building anything.

### 3. The Growth Flywheel
Focus on one channel until it works, then layer on the next.

## Metrics

- Monthly Recurring Revenue: $50,000
- Monthly Growth Rate: 15%
- Customer Acquisition Cost: $200
- Customer Lifetime Value: $8,000
- Churn Rate: 3%
- Active Users: 500
- Net Promoter Score: 72
"""


# ============================================================================
# Error Scenarios
# ============================================================================

VIDEO_NOT_FOUND_ERROR = {
    "error": {
        "code": 404,
        "message": "Video not found",
        "reason": "invalidVideoId"
    }
}


TRANSCRIPT_UNAVAILABLE_ERROR = {
    "error": "No transcript available for this video"
}


INVALID_URL_ERROR = {
    "error": "Invalid YouTube URL format"
}


# ============================================================================
# Helper Functions
# ============================================================================

def get_mock_youtube_response(video_id: str) -> Dict[str, Any]:
    """Get mock YouTube response for a given video ID."""
    response = MOCK_YOUTUBE_VIDEO_INFO.copy()
    response["id"] = video_id
    return response


def get_mock_transcript_text() -> str:
    """Get mock transcript text."""
    return MOCK_TRANSCRIPT_TEXT


def get_sample_markdown(filename: str = "sample.md") -> str:
    """Get sample markdown content."""
    return SAMPLE_RAW_TRANSCRIPT


def get_sample_profile(category: str = "Starter_Story") -> str:
    """Get sample processed profile for a category."""
    profiles = {
        "Starter_Story": SAMPLE_PROCESSED_PROFILE,
        "AI_Leaders": "# AI Thesis\n\nTest AI thesis content.",
        "Founders": "# Key Lessons\n\nTest founder lessons.\n\n## Books\n- Book 1\n- Book 2",
        "My_First_Million": "# Key Insights\n\nTest business insights.",
        "AI_Engineering": "# Core Framework\n\nTest technical framework.",
        "Inner_Work": "# Core Wisdom\n\nTest spiritual wisdom."
    }
    return profiles.get(category, SAMPLE_PROCESSED_PROFILE)