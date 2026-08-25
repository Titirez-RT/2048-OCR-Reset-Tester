# 2048 Automated Reset Test

An automated script that validates the reset functionality of a 2048 game using Optical Character Recognition (OCR).

## How It Works
1. Resets the game to start a fresh session.
2. Performs 10 random swipes to accumulate a score.
3. Triggers the reset function again.
4. Captures a screenshot of the score region.
5. Uses OCR to read the text and asserts that the score is successfully reset to `0`.

## Prerequisites
* Python
* An OCR engine
* UI automation and image processing libraries


<video src="Appium - 2048.mp4" width="600" controls autoplay loop muted></video>
