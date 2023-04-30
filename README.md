# Summarizing YouTube Video Transcripts using ChatGPT API

This Python script extracts the transcript from a YouTube video using the YouTubeTranscriptApi library and then uses OpenAI's ChatGPT API to summarize the transcript into bullet points highlighting key insights. The summarized transcript is then saved to a text file.
## Buy me a coffe
Whether you use this project, have learned something from it, or just like it, please consider supporting it by buying me a coffee, so I can dedicate more time on open-source projects like this :)

<a href="https://www.buymeacoffee.com/ascensao1" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-yellow.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Youtube

Check on Youtube: https://www.youtube.com/watch?v=lTYCBlL0ZH4&t

<img src="https://bernardoascensao.com/outsourcing/Stop_wasting_your_time.png" alt="See on Youtube" width="560" height="315" border="10"/>


## Dependencies

The script requires the following libraries to be installed:

- requests
- BeautifulSoup
- youtube_transcript_api
- openai

 ```pip install requests beautifulsoup4 youtube_transcript_api openai ```



## Usage

The script will prompt you to enter a YouTube video URL. Enter the URL and press Enter to begin the summarization process. Once the script finishes summarizing the transcript, it will save the summarized text to a text file in the current directory.

You can exit the script at any time by typing exit when prompted for a YouTube video URL.


## Notes

- The script uses OpenAI's GPT-3.5 Turbo model, which requires an API key to access. If you have a different OpenAI API key, you can modify the script to use a different model by changing the model_id variable in the script.
- The script splits the transcript into smaller chunks before sending them to the ChatGPT API for summarization. This is necessary because the API has a limit on the number of tokens that can be sent in a single request. You can modify the max_chunk_size variable in the script to adjust the size of the chunks.
- The script saves the summarized transcript to a text file with the video title and the suffix "_summary.txt". If the video title cannot be fetched, the script uses the video ID as the title.
- The script prints the total number of API tokens consumed during the summarization process.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
  

## Author

Bernardo Ascensao
