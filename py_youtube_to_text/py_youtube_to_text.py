import re
import os
import requests
import openai
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi


# Set OpenAI API Key
openai.api_key = 'you_api_here'
model_id = 'gpt-3.5-turbo'


# Extract the video id from URL
def extract_video_id(url):
    pattern = r"(?:https?:\/\/)?(?:www\.)?youtu(?:\.be\/|be\.com\/watch\?v=)([\w-]*)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None


# Get video title
def get_video_title(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title_element = soup.find("meta", itemprop="name")
    if title_element:
        return title_element["content"]
    else:
        return None


# Get all transcript from the video
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# ChatGPT Conversation
def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation


# Asking for chatGPT Summarize
def summarize_text(text):
    conversation = [{'role': 'system', 'content': 'Summarize the YouTube transcript in bullet points, highlighting key insights:'}]
    max_chunk_size = 2048 - len(conversation[0]['content']) - 100  # Reserve tokens for the prompt and model's response
    chunks = split_text_into_chunks(text, max_chunk_size)
    summarized_chunks = []

    total_tokens_used = 0  # Add a token counter

    for chunk in chunks:
        conversation.append({'role': 'user', 'content': chunk})
        response = openai.ChatCompletion.create(
            model=model_id,
            messages=conversation,
            max_tokens=100  # Limit the response length
        )
        api_usage = response['usage']
        print('Total token consumed: {0}'.format(api_usage['total_tokens']))

        summary = response.choices[0].message.content.strip()
        summarized_chunks.append(summary)

    return " ".join(summarized_chunks)


# Split the transcript into minor chunks pieces
def split_text_into_chunks(text, max_chunk_size):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(" ".join(current_chunk)) > max_chunk_size:
            current_chunk.pop()
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


# Save the summarized transcript into a .txt file
def save_to_txt(transcript, video_id, title):
    if transcript:
        if title is None:
            title = video_id
        full_text = "\n".join([item['text'] for item in transcript])
        summary = summarize_text(full_text)
        filename = f"{title}_summary.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(summary)
        print(f"Summary saved to {filename}")
    else:
        print("Could not save summary.")



# Run the script in a loop until the user enter the word "exit"
if __name__ == "__main__":
    while True:
        url = input("Please enter a YouTube video URL or type 'exit' to exit: ").strip()

        if url.lower() == 'exit':
            break

        video_id = extract_video_id(url)

        if video_id:
            title = get_video_title(video_id)
            if title:
                print(f"Video title: {title}")
            else:
                print("Could not fetch video title.")
            
            transcript = get_transcript(video_id)
            save_to_txt(transcript, video_id, title)
        else:
            print("Invalid YouTube URL. Please try again.")


