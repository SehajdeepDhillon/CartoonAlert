import os
from get_cartoon import get_latest_cartoon, is_new_cartoon
from send_cartoon import send_message
from analysis import analyze_cartoon

def handler():
    cartoon_url, cartoon_date = get_latest_cartoon()
    
    if not cartoon_url or not cartoon_date:
        print("Failed to get cartoon URL or date")
        return
    print(cartoon_url, cartoon_date)

    if cartoon_date and is_new_cartoon(cartoon_date):
        analysis = analyze_cartoon(cartoon_url)
        print("Analysis: ", analysis)

        message_content = f"New cartoon available! {cartoon_url}\nAnalysis: {analysis}"
        send_message(message_content)

if __name__ == "__main__":
    handler()