import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components
import random
import time

st.set_page_config(
    page_title="Siddhi Jeeee • The Birthday Universe",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE = Path(__file__).parent
ASSETS = BASE / "assets"

# -----------------------------
# State
# -----------------------------
defaults = {
    "stage": 0,
    "liked": False,
    "no_count": 0,
    "quiz_score": 0,
    "memory_choice": None,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# -----------------------------
# Premium styling + animations
# -----------------------------
st.markdown(r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=DM+Serif+Display&family=Manrope:wght@400;500;600;700;800&display=swap');
html,body,[data-testid="stAppViewContainer"]{
background:
radial-gradient(circle at 10% 8%,rgba(255,150,195,.28),transparent 25%),
radial-gradient(circle at 90% 15%,rgba(183,143,229,.25),transparent 28%),
radial-gradient(circle at 50% 100%,rgba(255,216,232,.5),transparent 30%),
linear-gradient(135deg,#fffaff,#fff1f7 55%,#f4effa);
}
[data-testid="stHeader"],[data-testid="stToolbar"]{background:transparent}
[data-testid="stToolbar"]{display:none}
.block-container{max-width:1150px;padding:1rem 1rem 4rem}
.hero{text-align:center;padding:.7rem 0 .4rem}
.kicker{font:800 11px Manrope;letter-spacing:4px;color:#b55a80}
.hero h1{font:700 clamp(42px,7vw,78px) 'DM Serif Display';color:#cf4b7b!important;margin:4px 0!important;text-shadow:0 10px 35px rgba(190,55,110,.15)}
.hero p,.sub{font:14px Manrope;color:#7a5869;text-align:center}
.glass{background:linear-gradient(135deg,rgba(255,255,255,.8),rgba(255,255,255,.43));border:1px solid rgba(255,255,255,.95);border-radius:30px;padding:25px;box-shadow:0 25px 70px rgba(88,30,65,.12),inset 0 1px 0 #fff;backdrop-filter:blur(18px);margin:16px 0}
.title{text-align:center;font:700 34px 'DM Serif Display';color:#7e3656}
.quote{text-align:center;font:600 clamp(22px,3vw,31px) 'Cormorant Garamond';color:#694456;line-height:1.35}
.big{text-align:center;font:700 clamp(27px,4vw,45px) 'DM Serif Display';color:#d84e80}
.progress{display:flex;gap:7px;justify-content:center;margin:5px 0 15px}
.dot{width:32px;height:7px;border-radius:20px;background:#f1d5e2}
.dot.on{background:#df5f8e;box-shadow:0 0 16px rgba(223,95,142,.45)}
.game{padding:20px;border-radius:24px;background:rgba(255,248,252,.75);border:1px solid #f3d3e1;margin:12px 0}
.game h3{font:700 23px 'DM Serif Display';color:#9c476b;text-align:center}
.answer{text-align:center;font:700 16px Manrope;color:#624354;padding:8px}
.memory{background:#fff8fc;border:1px solid #f1d6e2;border-radius:20px;padding:18px;color:#674555;font:14px Manrope;line-height:1.7}
.floating{position:fixed;inset:0;pointer-events:none;overflow:hidden;z-index:0}
.floating span{position:absolute;bottom:-70px;opacity:.4;font-size:22px;animation:rise linear infinite;filter:drop-shadow(0 8px 14px rgba(210,60,120,.18))}
.floating span:nth-child(1){left:3%;animation-duration:13s}.floating span:nth-child(2){left:12%;animation-duration:17s;animation-delay:-8s}.floating span:nth-child(3){left:24%;animation-duration:11s;animation-delay:-3s}.floating span:nth-child(4){left:37%;animation-duration:19s;animation-delay:-12s}.floating span:nth-child(5){left:51%;animation-duration:14s;animation-delay:-5s}.floating span:nth-child(6){left:64%;animation-duration:18s;animation-delay:-11s}.floating span:nth-child(7){left:77%;animation-duration:12s;animation-delay:-7s}.floating span:nth-child(8){left:91%;animation-duration:16s;animation-delay:-2s}
@keyframes rise{0%{transform:translate3d(0,0,0) rotate(0)}50%{transform:translate3d(22px,-45vh,0) rotate(18deg)}100%{transform:translate3d(-15px,-110vh,0) rotate(-12deg)}}
@keyframes pulse{50%{transform:scale(1.1)}}
.pulse{animation:pulse 1.8s ease-in-out infinite}
div.stButton>button{width:100%;border:0;border-radius:999px!important;padding:13px 18px!important;background:linear-gradient(90deg,#ec6b9d,#c94e7b)!important;color:#fff!important;font:800 13px Manrope!important;box-shadow:0 12px 30px rgba(201,78,123,.25)!important;transition:.25s}
div.stButton>button:hover{transform:translateY(-3px) scale(1.01)}
.no-btn div.stButton>button{background:linear-gradient(90deg,#aaa,#777)!important}
@media(max-width:700px){.glass{padding:17px}.title{font-size:28px}.hero h1{font-size:45px!important}}
</style>
<div class="floating"><span>♥</span><span>✦</span><span>♡</span><span>✧</span><span>♥</span><span>•</span><span>♡</span><span>✦</span></div>
""", unsafe_allow_html=True)

# -----------------------------
# 3D header
# -----------------------------
components.html("""
<html><style>
body{margin:0;background:transparent}.scene{height:180px;display:flex;justify-content:center;align-items:center;perspective:900px}
.h{width:78px;height:78px;transform:rotate(-45deg);background:linear-gradient(145deg,#ffb3cd,#d94e80);border-radius:17px;position:relative;animation:p 2.4s infinite;box-shadow:18px 25px 35px #8d3d5d55,inset 12px 12px 18px #ffffff66}
.h:before,.h:after{content:"";position:absolute;width:78px;height:78px;border-radius:50%;background:inherit}.h:before{top:-39px}.h:after{left:39px}
@keyframes p{50%{transform:rotate(-40deg) scale(1.12) translateZ(35px)}}
</style><div class="scene"><div class="h"></div></div></html>
""", height=195, scrolling=False)

st.markdown("""
<div class="hero">
<div class="kicker">WELCOME TO YOUR LITTLE UNIVERSE</div>
<h1>Siddhi Jeeee 💗</h1>
<p>Four stages. A few games. A tiny bit of mischief. And one very important question.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Stage 0: cinematic welcome
# -----------------------------
st.markdown('<div class="progress">' + ''.join(f'<span class="dot {"on" if i<=st.session_state.stage else ""}"></span>' for i in range(4)) + '</div>', unsafe_allow_html=True)

if st.session_state.stage == 0:
    st.markdown("""
    <div class="glass">
      <div class="title">🎁 Your birthday adventure starts here</div>
      <br>
      <div class="quote">
      “Some people enter your life as friends… and somehow become something much more.”
      </div>
      <br>
      <div class="sub">No rushing. Just tap your way through the little surprise I made for you. 🌷</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("✨ START THE SURPRISE"):
        st.session_state.stage = 1
        st.rerun()

# -----------------------------
# Stage 1: slideshow + memories
# -----------------------------
elif st.session_state.stage == 1:
    st.markdown('<div class="glass"><div class="title">📸 Chapter One — Little Moments</div><div class="sub">Swipe through the memories at your own pace.</div></div>', unsafe_allow_html=True)
    photos = [ASSETS / f"siddhi_0{i}.jpg" for i in range(1,5)]
    if "slide" not in st.session_state: st.session_state.slide = 0
    c1,c2,c3 = st.columns([1,3,1])
    with c1:
        if st.button("⬅️", key="prev"):
            st.session_state.slide = (st.session_state.slide-1)%4
            st.rerun()
    with c2:
        st.image(str(photos[st.session_state.slide]), use_container_width=True)
    with c3:
        if st.button("➡️", key="next"):
            st.session_state.slide = (st.session_state.slide+1)%4
            st.rerun()
    st.markdown(f'<div class="sub">Photo {st.session_state.slide+1} / 4</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="game">
      <h3>🌙 Memory Match</h3>
      <div class="answer">Which one feels most “us”?</div>
    </div>
    """, unsafe_allow_html=True)
    opts = ["Late-night talks 🌙","Sharing everything 💭","Caring for each other 🫶","That Jharkhandi accent 😂"]
    cols = st.columns(2)
    for i,opt in enumerate(opts):
        with cols[i%2]:
            if st.button(opt, key=f"mem{i}"):
                st.session_state.memory_choice = opt
                st.toast("Memory saved in the tiny universe 💗")
    if st.session_state.memory_choice:
        st.markdown(f'<div class="memory"><b>Your pick:</b> {st.session_state.memory_choice}<br>Honestly… every one of these belongs here. ❤️</div>', unsafe_allow_html=True)
    st.write("")
    if st.button("🎮 NEXT: LET'S PLAY"):
        st.session_state.stage = 2
        st.rerun()

# -----------------------------
# Stage 2: mini games
# -----------------------------
elif st.session_state.stage == 2:
    st.markdown('<div class="glass"><div class="title">🎮 Chapter Two — Siddhi Games</div><div class="sub">Three tiny games. Zero serious competition. 😌</div></div>', unsafe_allow_html=True)

    # Game 1
    st.markdown('<div class="game"><h3>💗 Game 1 — Pick Your Vibe</h3></div>', unsafe_allow_html=True)
    vibe = st.radio("Choose one:", ["🌙 Midnight talks", "🌸 Cute chaos", "🎧 Music & vibes", "☕ Random conversations"], horizontal=False, key="vibe")
    if st.button("Lock my vibe 🔒", key="vibe_btn"):
        st.success(f"Excellent choice: {vibe}")

    # Game 2
    st.markdown('<div class="game"><h3>🧠 Game 2 — How well do you know this surprise?</h3></div>', unsafe_allow_html=True)
    q = st.selectbox("What had to appear in this app?", ["A boring spreadsheet", "Your Jharkhandi accent 😂", "A tax calculator", "A weather report"], key="quiz")
    if st.button("Check answer ✨", key="quiz_btn"):
        if q == "Your Jharkhandi accent 😂":
            st.session_state.quiz_score = 1
            st.balloons()
            st.success("Correct! 😂❤️ Obviously this was mandatory.")
        else:
            st.session_state.quiz_score = 0
            st.warning("Nope 😭 Try again.")

    # Game 3
    st.markdown('<div class="game"><h3>🎲 Game 3 — Lucky Heart</h3></div>', unsafe_allow_html=True)
    if st.button("✨ Pick a random heart", key="heart_game"):
        prizes = ["A virtual hug 🫂","1000 smiles 😊","Unlimited late-night talks 🌙","A lifetime supply of good vibes ✨","One very special birthday message 💌"]
        st.success("You got: " + random.choice(prizes))

    st.write("")
    if st.button("💌 NEXT: THERE'S ONE MORE THING"):
        st.session_state.stage = 3
        st.rerun()

# -----------------------------
# Stage 3: question gate
# -----------------------------
elif st.session_state.stage == 3:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown('<div class="title">💌 Chapter Three — One Honest Question</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="quote">
    Before the last page opens, I have one slightly dangerous question… 😌
    </div><br>
    <div class="big">Kshitiz — I like uh? 💗</div>
    <br>
    <div class="sub">
    Choose honestly. If you choose “I don't like uh”, the app will stay here and give you a playful response.
    The next chapter opens only when you choose “I like uh”. 🌷
    </div>
    """, unsafe_allow_html=True)

    a,b = st.columns(2)
    with a:
        if st.button("💗 I LIKE UH", key="like"):
            st.session_state.liked = True
            st.session_state.stage = 4
            st.rerun()
    with b:
        if st.button("😶 I DON'T LIKE UH", key="dont"):
            st.session_state.no_count += 1
            st.warning("Ohooo 😭😂 Nice try. The final chapter is still locked. Choose when you're ready. 💗")

    if st.session_state.no_count:
        st.markdown(f'<div class="sub">Playful attempts to escape: {st.session_state.no_count} 😭</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Stage 4: final reveal
# -----------------------------
else:
    st.balloons()
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown('<div class="title">✨ Final Chapter — You Unlocked It</div>', unsafe_allow_html=True)
    st.markdown('<div class="big pulse">YOU SAID YES TO THE SURPRISE. ❤️</div><br>', unsafe_allow_html=True)

    video = ASSETS / "birthday_video.mp4"
    if video.exists():
        st.video(str(video))

    st.markdown("""
    <div class="quote">
    Siddhi jeeee… ❤️<br><br>
    You're not just my best friend. You're someone who became
    a much bigger and more beautiful part of my life than I ever expected.
    </div><br>
    <div class="quote">
    From late-night talks and sharing thoughts and feelings,
    to caring for you and laughing about your Jharkhandi accent 😂 —
    these little things mean more to me than I can properly explain.
    </div><br>
    <div class="big">I'M GENUINELY BLESSED TO HAVE YOU. ✨</div><br>
    <div class="quote">
    Happy Birthday, Siddhi Jeeee. 🌷<br>
    Keep smiling. Keep shining. Keep being you.
    </div>
    """, unsafe_allow_html=True)

    if (ASSETS / "siddhi_bitmoji_stickers.png").exists():
        st.image(str(ASSETS / "siddhi_bitmoji_stickers.png"), use_container_width=True)

    if st.button("🔄 Replay from the beginning"):
        for k,v in defaults.items():
            st.session_state[k]=v
        st.rerun()

st.markdown("""
<div style="text-align:center;padding:24px;color:#9a7182;font:12px Manrope">
Made with an unreasonable amount of care for Siddhi Jeeee 💗
</div>
""", unsafe_allow_html=True)
