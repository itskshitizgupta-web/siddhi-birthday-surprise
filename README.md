# 🎀 Siddhi Birthday Surprise

A cute interactive Streamlit birthday website for Siddhi.

## Folder structure

```text
siddhi_birthday_surprise/
├── app.py
├── requirements.txt
├── README.md
└── assets/
    ├── photo1.jpg
    ├── photo2.jpg
    └── birthday_music.mp3   # optional
```

Put Siddhi's photos in `assets/`. The app automatically finds JPG, JPEG, PNG and WEBP files.

## Run on your computer

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy for a shareable link

1. Create a GitHub repository, e.g. `siddhi-birthday-surprise`.
2. Upload `app.py`, `requirements.txt`, and the entire `assets` folder.
3. Open https://share.streamlit.io/
4. Sign in with GitHub.
5. Click **Create app**.
6. Select your repository, branch (`main`) and `app.py`.
7. Choose a memorable custom subdomain if available.
8. Deploy.

Your final link will look like:

https://your-custom-name.streamlit.app/

Send that link to Siddhi. 💗

## Personalize more

Edit the questions, captions and letter directly in `app.py`.
