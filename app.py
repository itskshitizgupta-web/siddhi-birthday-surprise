import streamlit as st
from pathlib import Path
import base64
import random

# -----------------------------
# Siddhi Birthday Surprise 🎀
# -----------------------------
st.set_page_config(
    page_title="Siddhi's Birthday Surprise 💗",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Helpers ----------
ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

def local_images():
    extensions = {".jpg", ".jpeg", ".png", ".webp"}
    images = []
    for p in ROOT.rglob("*"):
        if p.is_file() and p.suffix.lower() in extensions:
            images.append(p)
    return sorted(images)

def image_data_uri(path):
    mime = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
    }.get(path.suffix.lower(), "image/jpeg")
    encoded = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime};base64,{encoded}"

# ---------- Session state ----------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = set()
if "final_revealed" not in st.session_state:
    st.session_state.final_revealed = False

# ---------- CSS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}
.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(255,255,255,.75) 0 2px, transparent 3px),
        radial-gradient(circle at 90% 20%, rgba(255,255,255,.55) 0 2px, transparent 3px),
        linear-gradient(135deg, #fff0f6 0%, #ffe4ef 45%, #f6e9ff 100%);
    background-size: 85px 85px, 120px 120px, auto;
}
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}
.hero {
    padding: 45px 25px 35px;
    border-radius: 35px;
    text-align: center;
    background: rgba(255,255,255,.68);
    border: 1px solid rgba(255,255,255,.9);
    box-shadow: 0 18px 60px rgba(180, 80, 130, .15);
    backdrop-filter: blur(12px);
}
.script {
    font-family: 'Pacifico', cursive;
    font-size: clamp(2.7rem, 8vw, 5.8rem);
    color: #d94d86;
    line-height: 1.05;
}
.subtitle {
    font-size: 1.05rem;
    color: #6d4d60;
}
.card {
    padding: 25px;
    border-radius: 25px;
    background: rgba(255,255,255,.72);
    border: 1px solid rgba(255,255,255,.9);
    box-shadow: 0 10px 35px rgba(150,70,110,.10);
    margin: 12px 0;
}
.quote {
    font-size: 1.15rem;
    line-height: 1.8;
    color: #5d4051;
}
.memory {
    padding: 18px;
    border-radius: 22px;
    background: rgba(255,255,255,.7);
    margin-bottom: 15px;
}
.big-heart {
    font-size: 4rem;
    animation: pulse 1.8s infinite;
}
@keyframes pulse {
    0%,100% { transform: scale(1); }
    50% { transform: scale(1.12); }
}
.confetti {
    font-size: 2.1rem;
    letter-spacing: 12px;
}
.small {
    color: #856477;
    font-size: .9rem;
}

/* Bright, readable birthday game cards */
.game-card {
    background: #ffffff !important;
    color: #351b2d !important;
    border-radius: 24px;
    padding: 24px;
    margin: 14px 0;
    box-shadow: 0 10px 30px rgba(100, 35, 75, .12);
    border: 2px solid #ffd1e3;
}
.game-card h2, .game-card h3, .game-card p, .game-card b {
    color: #351b2d !important;
}
.game-title {
    color: #b52f6d !important;
    font-weight: 700;
}
</style>

""", unsafe_allow_html=True)

# ---------- Navigation ----------
def nav():
    cols = st.columns(5)
    labels = [("🏠", "home"), ("🎮", "game"), ("📸", "memories"), ("💌", "letter"), ("🎉", "final")]
    for col, (icon, page) in zip(cols, labels):
        with col:
            if st.button(icon, key=f"nav_{page}", use_container_width=True):
                st.session_state.page = page
                st.rerun()

nav()

# ---------- HOME ----------
if st.session_state.page == "home":
    st.markdown("""
    <div class="hero">
        <div style="font-size:2rem">🎀 🧸 🌷 ✨ 🎂 ✨ 🌷 🧸 🎀</div>
        <div class="script">Happy Birthday</div>
        <div class="script" style="font-size:clamp(2.5rem,7vw,5rem)">Siddhi 💗</div>
        <p class="subtitle">
            I made this little corner of the internet just for you, Siddhi. ❤️
            Take your time... there are a few surprises waiting. 🥹
        </p>
    </div>
    """, unsafe_allow_html=True)

    imgs = local_images()
    if imgs:
        st.image(str(imgs[0]), use_container_width=True)
        st.caption("One of my favourite memories with you. ❤️")
    else:
        st.markdown("""
        <div class="card" style="text-align:center">
            <div style="font-size:5rem">🎂</div>
            <h2>Today is YOUR day! 🥳</h2>
            <p class="quote">Add your favourite Siddhi photos to the <b>assets</b> folder and they'll appear here automatically.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>🌸 Before you start...</h2>
        <p class="quote">
        Siddhi, I just want you to know one thing:
        <b>I feel genuinely blessed to have you in my life.</b> ❤️
        </p>
        <p class="quote">
        You are strong. You are brave. And you are capable of achieving
        anything you truly want. Never forget how much potential you have. ✨
        </p>
        <p class="quote">
        So today, forget everything for a little while, smile,
        and enjoy this tiny surprise made especially for you. 🫶
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💌 Start the surprise", use_container_width=True, type="primary"):
        st.session_state.page = "game"
        st.rerun()

# ---------- GAME ----------
elif st.session_state.page == "game":
    st.markdown("""
    <div class="hero">
        <div class="script" style="font-size:3.4rem">Siddhi's Lucky Heart Challenge 💗</div>
        <p class="subtitle">Pick a heart, answer a few surprises, and unlock your birthday message! ✨</p>
    </div>
    """, unsafe_allow_html=True)

    if "heart_round" not in st.session_state:
        st.session_state.heart_round = 1
    if "heart_wins" not in st.session_state:
        st.session_state.heart_wins = 0
    if "heart_target" not in st.session_state:
        st.session_state.heart_target = random.randint(1, 6)
    if "heart_message" not in st.session_state:
        st.session_state.heart_message = ""

    st.markdown(f"""
    <div class="game-card">
      <h2 class="game-title">💗 Round {st.session_state.heart_round} / 3</h2>
      <p><b>Find the lucky heart!</b> One of these six hearts hides a special surprise.</p>
      <p>Lucky hearts found: <b>{st.session_state.heart_wins}</b> 🌟</p>
    </div>
    """, unsafe_allow_html=True)

    heart_cols = st.columns(6)
    for i, col in enumerate(heart_cols, start=1):
        with col:
            if st.button("💗", key=f"heart_{st.session_state.heart_round}_{i}", use_container_width=True):
                if i == st.session_state.heart_target:
                    st.session_state.heart_wins += 1
                    st.session_state.heart_message = "🎉 You found it! Just like you, this heart was impossible to miss. ❤️"
                else:
                    st.session_state.heart_message = "😂 Oops! Not this one. Try another heart!"

                if st.session_state.heart_round < 3:
                    st.session_state.heart_round += 1
                    st.session_state.heart_target = random.randint(1, 6)
                else:
                    st.session_state.heart_round = 4
                st.rerun()

    if st.session_state.heart_message:
        st.markdown(f"""
        <div class="game-card" style="text-align:center">
          <h3>{st.session_state.heart_message}</h3>
        </div>
        """, unsafe_allow_html=True)

    if st.session_state.heart_round >= 4:
        st.balloons()
        st.markdown("""
        <div class="game-card" style="text-align:center">
          <h2 class="game-title">🎁 Challenge Complete!</h2>
          <p style="font-size:1.1rem">
          Siddhi, whether you found every lucky heart or not, here's the real truth:
          <b>you are one of the luckiest things that happened in my life, and I feel blessed to have you. ❤️</b>
          </p>
          <p style="font-size:1.05rem">
          You are strong, brave and capable of achieving anything you set your heart on. 🌟
          </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔄 Play the heart challenge again", use_container_width=True):
            st.session_state.heart_round = 1
            st.session_state.heart_wins = 0
            st.session_state.heart_target = random.randint(1, 6)
            st.session_state.heart_message = ""
            st.rerun()

        if st.button("📸 Unlock the memories", use_container_width=True, type="primary"):
            st.session_state.page = "memories"
            st.rerun()
    else:
        st.markdown("""
        <div class="game-card">
          <h3 class="game-title">🌷 Bonus question</h3>
          <p><b>What should Siddhi always remember?</b></p>
          <p>💪 She is strong &nbsp; • &nbsp; 🦁 She is brave &nbsp; • &nbsp; 🌟 She can achieve what she wants</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("💌 Give me the next surprise", use_container_width=True):
            st.session_state.page = "memories"
            st.rerun()

# ---------- MEMORIES ----------
elif st.session_state.page == "memories":
    st.markdown('<div class="hero"><div class="script" style="font-size:3.5rem">Our Little Memories 📸</div><p class="subtitle">Every picture has a story. Every story has a little piece of us.</p></div>', unsafe_allow_html=True)

    imgs = local_images()
    if not imgs:
        st.info("📂 No photos found yet. Put JPG/PNG/WEBP photos inside the app's `assets` folder, then refresh the page.")
    else:
        captions = [
            "One of my favourite memories with you. ❤️",
            "That smile deserves its own little corner here. 🌷",
            "A beautiful moment that I am glad I get to remember. ✨",
            "One more chapter in our little collection of memories. 💗",
            "Some pictures become memories; some memories become priceless. 🥹",
        ]
        for i, img in enumerate(imgs):
            st.markdown('<div class="memory">', unsafe_allow_html=True)
            st.image(str(img), use_container_width=True)
            st.markdown(f"<p class='quote'><b>Memory {i+1} 🌸</b><br>{captions[i % len(captions)]}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
      <h2>🌙 And then there are the memories no camera can capture...</h2>
      <p class="quote">
      The random conversations. The laughs. The moments when we talked about
      everything and nothing. Those are some of the memories I value the most.
      ❤️
      </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💌 Read my message", use_container_width=True):
        st.session_state.page = "letter"
        st.rerun()

# ---------- LETTER ----------
elif st.session_state.page == "letter":
    st.markdown('<div class="hero"><div class="big-heart">💗</div><div class="script" style="font-size:3.4rem">A Letter for Siddhi</div></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <p class="quote"><b>Dear Siddhi,</b> 🌷</p>

    <p class="quote">
    I don't know if a website can ever properly explain how much someone means
    to you, but I wanted to try.
    </p>

    <p class="quote">
    I genuinely feel <b>blessed to have you in my life.</b> ❤️
    Thank you for being someone I can talk to, laugh with, share things with,
    and simply be myself around.
    </p>

    <p class="quote">
    I hope you never underestimate yourself. You are <b>strong</b>, you are
    <b>brave</b>, and you have so much more potential than you sometimes
    realise.
    </p>

    <p class="quote">
    Whatever dream you choose, whatever path you take, I hope you chase it
    fearlessly. <b>You can achieve anything you truly want.</b> ✨
    </p>

    <p class="quote">
    Keep smiling. Keep being the person you are. And when life gets difficult,
    remember that difficult days don't define you — the way you keep going does.
    🫶
    </p>

    <p class="quote">
    Happy Birthday, Siddhi. 🎂<br>
    May this year bring you beautiful memories, big achievements,
    peaceful moments and countless reasons to smile.
    </p>

    <p class="quote"><b>I'm really lucky to have you. ❤️</b></p>
    <p style="text-align:right;font-size:1.1rem">— From someone who cares about you a lot 🌸</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card" style="text-align:center">
      <h2>🎁 There's still one last surprise...</h2>
      <p class="quote">Don't click the button unless you're ready. 👀</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("✨ One Last Thing...", use_container_width=True, type="primary"):
        st.session_state.page = "final"
        st.session_state.final_revealed = True
        st.rerun()

# ---------- FINAL ----------
elif st.session_state.page == "final":
    if st.session_state.final_revealed:
        st.balloons()

    st.markdown("""
    <div class="hero">
        <div class="confetti">🎉 ✨ 🎊 💗 🎊 ✨ 🎉</div>
        <div class="script" style="font-size:clamp(3rem,9vw,6rem)">HAPPY BIRTHDAY</div>
        <div class="script" style="font-size:clamp(3rem,9vw,6rem)">NANDANA! 💗</div>
        <div class="confetti">🌷 🧸 🎂 🫶 🎂 🧸 🌷</div>
        <p class="quote">
            You deserve all the happiness, love, success and beautiful things
            life has to offer. ✨
        </p>
        <p class="quote"><b>Never stop believing in yourself. ❤️</b></p>
    </div>
    """, unsafe_allow_html=True)

    imgs = local_images()
    if imgs:
        st.markdown("### 📸 One final look at some favourite moments")
        cols = st.columns(min(3, len(imgs)))
        for i, img in enumerate(imgs[:6]):
            with cols[i % len(cols)]:
                st.image(str(img), use_container_width=True)

    st.markdown("""
    <div class="card" style="text-align:center">
      <div class="big-heart">❤️</div>
      <h2>Siddhi, I'm blessed to have you.</h2>
      <p class="quote">
      Stay strong. Stay brave. Dream big.<br>
      And go achieve everything your heart wants. 🌟
      </p>
      <p class="small">Made with a ridiculous amount of love, effort and probably too many emojis. 😂💗</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔁 Replay from the beginning", use_container_width=True):
        st.session_state.page = "home"
        st.session_state.score = 0
        st.session_state.answered = set()
        st.session_state.final_revealed = False
        st.rerun()

# ---------- Optional music ----------
st.markdown("---")
st.markdown("### 🎵 Birthday music")
music = ASSETS / "birthday_music.mp3"
if music.exists():
    st.audio(str(music))
else:
    st.caption("Optional: put a file named `birthday_music.mp3` inside the `assets` folder to add music.")
