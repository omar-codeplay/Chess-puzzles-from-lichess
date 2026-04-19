import requests
import json
import time
import os

def download_and_split(target_total=10000, chunk_size=2000):
    url = "https://datasets-server.huggingface.co/rows"
    all_puzzles = []
    offset = 0
    file_count = 1
    
    print(f"🚀 Starting download of {target_total} puzzles in chunks of {chunk_size}...")

    while len(all_puzzles) < target_total:
        params = {
            "dataset": "Lichess/chess-puzzles",
            "config": "default",
            "split": "train",
            "offset": offset,
            "length": 100
        }
        
        try:
            r = requests.get(url, params=params)
            r.raise_for_status()
            batch = [item["row"] for item in r.json()["rows"]]
            all_puzzles.extend(batch)
            
            print(f"✅ Fetched {len(all_puzzles)}/{target_total}")
            offset += 100

            # --- SAVE EVERY 2000 ---
            if len(all_puzzles) % chunk_size == 0:
                filename = f"puzzles_part_{file_count}.json"
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(all_puzzles[-chunk_size:], f)
                print(f"💾 Saved {filename}. Waiting 10 seconds...")
                file_count += 1
                time.sleep(15)
            else:
                # Standard 1-second wait between 100-row batches
                time.sleep(3)
                
        except Exception as e:
            print(f"❌ Error: {e}")
            break

    print("\n✨ All chunks downloaded and saved!")

if __name__ == "__main__":
    download_and_split(40000, 2000)
