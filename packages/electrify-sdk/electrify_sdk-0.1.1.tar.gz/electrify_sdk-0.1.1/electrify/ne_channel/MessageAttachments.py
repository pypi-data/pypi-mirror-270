import httpx
import asyncio
from pathlib import Path

class MessageAttachments:
    def __init__(self, output_directory):
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists

    async def download_file(self, url):
        # Extract the unique identifier and the filename from the URL
        # Split URL by '--', take the second part, then split by '/' and take the last part for filename
        parts = url.split('--')
        if len(parts) > 1:
            unique_id = parts[1].split('/')[0]  # Unique ID before the filename
            filename = parts[1].split('/')[-1]  # Actual filename
            safe_filename = f"{unique_id}-{filename}"  # Combine with hyphen
        else:
            safe_filename = "default_filename.pdf"  # Fallback filename if URL format is unexpected

        file_path = self.output_directory / safe_filename

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, follow_redirects=True)
                response.raise_for_status()  # Check for HTTP errors

                # Write the content to the file
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f"Download Completed for {safe_filename}")
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e.response.status_code}")
        except httpx.RequestError as e:
            print(f"Request error occurred: {e.message}")
            if file_path.exists():
                file_path.unlink()  # Delete the file if an error occurs

