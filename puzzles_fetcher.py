import requests
import json
import time
import os
import glob

PROGRESS_FILE = "download_progress.json"

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return None  # مش default — عشان نفرّق بين "ملف موجود" و"مافيش ملف"

def save_progress(offset, total_saved, file_count, target_total):
    with open(PROGRESS_FILE, "w") as f:
        json.dump({
            "offset": offset,
            "total_saved": total_saved,
            "file_count": file_count,
            "target_total": target_total   # ← جديد
        }, f)

def detect_existing_state():
    """لو مافيش progress file، نحسب الوضع من الملفات الموجودة"""
    files = sorted(glob.glob("puzzles_part_*.json"))
    if not files:
        return 0, 0, 1  # offset, total_saved, file_count

    total_saved = 0
    for f in files:
        try:
            with open(f, "r") as fp:
                data = json.load(fp)
                total_saved += len(data)
        except:
            pass

    file_count = len(files) + 1
    offset = total_saved  # الـ API offset = عدد الـ puzzles المحفوظة
    return offset, total_saved, file_count

def download_and_split(target_total=150000, chunk_size=2000):
    url = "https://datasets-server.huggingface.co/rows"

    progress = load_progress()

    if progress is not None:
        offset      = progress["offset"]
        total_saved = progress["total_saved"]
        file_count  = progress["file_count"]
        saved_target = progress.get("target_total", target_total)

        if saved_target != target_total:
            # المستخدم غيّر الـ target → كمّل من نفس المكان بالـ target الجديد
            print(f"⚠️  Target changed: {saved_target} → {target_total}. Resuming from {total_saved}...")
        else:
            print(f"🔄 Resuming from offset {offset} ({total_saved}/{target_total} puzzles saved)...")

    else:
        # مافيش ملف تقدم → نشوف لو في ملفات موجودة
        offset, total_saved, file_count = detect_existing_state()

        if total_saved > 0:
            print(f"📂 No progress file, but found {total_saved} puzzles in existing files.")
            print(f"   Resuming from puzzle #{total_saved + 1}...")
        else:
            print(f"🚀 Fresh start — downloading {target_total} puzzles in chunks of {chunk_size}...")

    if total_saved >= target_total:
        print(f"✅ Already have {total_saved} puzzles, nothing to do!")
        return

    buffer = []

    while total_saved + len(buffer) < target_total:
        params = {
            "dataset": "Lichess/chess-puzzles",
            "config":  "default",
            "split":   "train",
            "offset":  offset,
            "length":  100
        }

        try:
            r = requests.get(url, params=params, timeout=30)
            r.raise_for_status()
            batch = [item["row"] for item in r.json()["rows"]]

            if not batch:
                print("⚠️ API returned no more data.")
                break

            buffer.extend(batch)
            offset += 100
            current_total = total_saved + len(buffer)
            print(f"✅ Fetched {current_total}/{target_total}  (buffer: {len(buffer)})")

            # احفظ كل ما يكتمل chunk
            while len(buffer) >= chunk_size:
                chunk   = buffer[:chunk_size]
                buffer  = buffer[chunk_size:]

                filename = f"puzzles_part_{file_count}.json"
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(chunk, f)

                total_saved += chunk_size
                file_count  += 1
                save_progress(offset, total_saved, file_count, target_total)

                print(f"💾 Saved {filename} ({total_saved}/{target_total}). Waiting 15s...")
                time.sleep(15)
            else:
                time.sleep(3)

        except KeyboardInterrupt:
            print("\n⏸️ Interrupted! Saving progress...")
            save_progress(offset, total_saved, file_count, target_total)
            print(f"✅ Saved. Run again to resume from puzzle #{total_saved + 1}.")
            return

        except Exception as e:
            print(f"❌ Error: {e}. Saving progress and retrying in 30s...")
            save_progress(offset, total_saved, file_count, target_total)
            time.sleep(30)
            continue

    # احفظ الباقي في الـ buffer
    if buffer:
        filename = f"puzzles_part_{file_count}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(buffer, f)
        total_saved += len(buffer)
        file_count  += 1
        print(f"💾 Saved final {filename} ({len(buffer)} puzzles)")

    save_progress(offset, total_saved, file_count, target_total)
    print(f"\n✨ Done! {total_saved} puzzles across {file_count - 1} files.")

if __name__ == "__main__":
    download_and_split(150000, 2000)