For BC Hacks 6

## Table of Contents

- [Recipe Receptionist](#recipe-receptionist)
  - [Inspiration](#inspiration)
  - [What it does](#what-it-does)
    - [For accessibility](#for-accessibility)
  - [How we built it](#how-we-built-it)
  - [Challenges we ran into](#challenges-we-ran-into)
  - [Accomplishments that we're proud of](#accomplishments-that-were-proud-of)
  - [What we learned](#what-we-learned)
- [Setup](#setup)
  
# Recipe Receptionist

![DFD Diagram](docs/DFD.jpg)

## Inspiration

We created Recipe Receptionist to solve the frustration of finding specific moments in long videos, like key lecture examples or unique cooking tips. We also wanted to make video content more accessible for people with disabilities, such as those with visual or hearing impairments, who often struggle to access or interpret videos.

## What it does

The app lets users upload a video or paste a URL. It analyzes the video frame by frame, transcribes the audio, and lets users ask specific questions about the content. For example:

Students can ask, "What was the example problem solved at 30 minutes?"

Cooking enthusiasts can ask, "What was the chef’s secret tip?"

### For accessibility

Visually impaired users: Get audio descriptions of visual content.

Hearing-impaired users: Receive accurate transcriptions and visual summaries.

Cognitive disabilities: Simplifies complex video content into easy-to-understand answers.

## How we built it

Frontend: Streamlit for a simple interface.

Backend: Python for video and audio processing.

APIs: OpenAI’s Whisper for transcription and GPT-4 for answering questions.

Video Processing: OpenCV for frames and FFmpeg for audio extraction.

URL Handling: you-get to download videos from URLs.

## Challenges we ran into

Slow video processing for long videos.

API rate limits from OpenAI.

Ensuring accessibility for disabled users.

Handling large video files and different formats.

## Accomplishments that we're proud of

Integrating multiple technologies into a seamless app.

Making video content more accessible and inclusive.

Building a functional prototype quickly.

Positive feedback from the accessibility community.

There are many image detection/analysing apps but not many video ones, so this is in a league of it's own

## What we learned

Balancing performance and accuracy in video processing.

How AI can make content more inclusive.

Handling large datasets and optimizing efficiency.

The importance of user feedback for improvement.

What's next for Recipe Receptionist
Better Accessibility: Add sign language interpretation, text-to-speech, and real-time captions.

Faster Performance: Optimize processing for longer videos.

Smarter AI: Add summarization, keyword search, and emotion analysis.

User Customization: Let users adjust settings like frame rate and language.

Platform Integration: Work with YouTube, Vimeo, and Coursera.

Community Collaboration: Open-source the project and partner with accessibility organizations.

# Setup

Requirements:

* mmfpeg installed on device
* all python modules in ```requirements.txt```. You can run ```pip3 install -r requirements.txt``` in the root directory to download them all.
* you **MUST** have the following evironment variable: ```OPENAI_API_KEY=<YOUR_API_KEY>```. Set this in your respective shell.
- To run the app: ```streamlit run app.py```