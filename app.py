import streamlit as st
from pathlib import Path
import base64
import random
import time

# ============================================================
# SIDDHI JEEEE 💗 — Cinematic Birthday Experience
# Streamlit-ready | Put this app.py beside the assets folder
# ============================================================

st.set_page_config(
    page_title="For Siddhi Jeeee 💗",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

# -------------------- Helpers --------------------
def local_images():
    exts = {".jpg", ".jpeg", ".png", ".webp"}
    return sorted([p for p in ASSETS.glob("*") if p.is_file() and p.suffix.lower() in exts])


def data_uri(path: Path):
    mime = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}.get(path.suffix.lower(), "image/jpeg")
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def safe_img(path: Path, cls="photo"):
    return f'<img class="{cls}" src="{data_uri(path)}" alt="Siddhi memory">'


def go(page):
    st.session_state.page = page
    st.rerun()

# -------------------- State --------------------
if "page" not in st.session_state:
    st.session_state.page = "intro"
if "opened" not in st.session_state:
    st.session_state.opened = False
if "love_meter" not in st.session_state:
    st.session_state.love_meter = 0
if "memory" not in st.session_state:
    st.session_state.memory = 0
if "final" not in st.session_state:
    st.session_state.final = False
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

imgs = local_images()

# -------------------- Global CSS / Animation Engine --------------------
st.markdown(r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Serif+Display&family=Manrope:wght@400;500;600;700&display=swap');

:root{
 --rose:#e85d8c; --rose2:#ff86ad; --wine:#7d3455; --ink:#3d2734;
 --cream:#fffafc; --glass:rgba(255,255,255,.67);
}

*{box-sizing:border-box}
html,body,[class*="css"]{font-family:'Manrope',sans-serif}
.stApp{
 min-height:100vh;
 background:
 radial-gradient(circle at 15% 15%,rgba(255,151,192,.20),transparent 27%),
 radial-gradient(circle at 85% 12%,rgba(184,151,255,.18),transparent 25%),
 radial-gradient(circle at 50% 100%,rgba(255,210,228,.25),transparent 35%),
 linear-gradient(135deg,#fff9fc 0%,#fff0f7 48%,#f8f1ff 100%);
 overflow-x:hidden;
}
.block-container{max-width:1180px;padding-top:1rem;padding-bottom:5rem}

/* Cinematic floating layer */
.fx{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}
.orb{position:absolute;border-radius:50%;filter:blur(2px);opacity:.55;animation:drift 14s ease-in-out infinite}
.orb.o1{width:180px;height:180px;background:#ffd0e1;left:-50px;top:18%;animation-delay:-2s}
.orb.o2{width:240px;height:240px;background:#e8d4ff;right:-70px;top:35%;animation-delay:-7s}
.orb.o3{width:120px;height:120px;background:#ffe6ba;left:45%;bottom:-35px;animation-delay:-4s}
@keyframes drift{0%,100%{transform:translate3d(0,0,0) scale(1)}50%{transform:translate3d(35px,-45px,0) scale(1.08)}}

.particle{position:absolute;bottom:-50px;opacity:0;animation:floatUp linear infinite}
@keyframes floatUp{0%{transform:translateY(0) rotate(0deg) scale(.7);opacity:0}12%{opacity:.75}80%{opacity:.55}100%{transform:translateY(-115vh) rotate(260deg) scale(1.25);opacity:0}}

/* Glass / premium cards */
.glass,.hero,.letter,.memory-card,.final-card,.timeline-card{
 position:relative;z-index:2;
 background:var(--glass);border:1px solid rgba(255,255,255,.85);
 box-shadow:0 25px 80px rgba(125,52,85,.13), inset 0 1px 0 rgba(255,255,255,.85);
 backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);
 border-radius:32px;
}
.hero{text-align:center;padding:clamp(32px,6vw,70px) 24px;margin:10px 0 24px;overflow:hidden}
.hero:before{content:"";position:absolute;inset:-2px;border-radius:34px;padding:2px;background:linear-gradient(120deg,rgba(255,255,255,.8),rgba(232,93,140,.25),rgba(220,197,255,.45),rgba(255,255,255,.8));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;animation:borderGlow 5s linear infinite}
@keyframes borderGlow{to{filter:hue-rotate(360deg)}}
.kicker{letter-spacing:5px;text-transform:uppercase;color:#aa5678;font-size:11px;font-weight:700}
.script{font-family:'DM Serif Display',serif;color:#d54f7f;font-size:clamp(3.1rem,8vw,7.2rem);line-height:.95;text-shadow:0 8px 35px rgba(213,79,127,.18)}
.script.small{font-size:clamp(2.5rem,6vw,5.3rem)}
.subtitle{color:#725365;font-size:clamp(.9rem,2vw,1.08rem);line-height:1.8;max-width:720px;margin:18px auto}
.pill{display:inline-block;padding:9px 15px;border-radius:999px;background:rgba(255,255,255,.78);color:#9b4c70;font-size:12px;font-weight:700;margin:5px;border:1px solid #f5d2e0}

.section-title{font-family:'DM Serif Display',serif;color:#8f4163;font-size:clamp(2rem,5vw,3.4rem);text-align:center;margin:30px 0 10px}
.center{text-align:center}
.card-pad{padding:28px}
.quote{font-family:'Cormorant Garamond',serif;color:#573c4b;font-size:clamp(1.15rem,2vw,1.45rem);line-height:1.7}
.body{color:#634957;line-height:1.9;font-size:15px}

/* Photo treatment */
.photo-wrap{position:relative;overflow:hidden;border-radius:28px;background:#fff;padding:8px;box-shadow:0 20px 50px rgba(91,40,65,.16);transform:rotate(-.7deg);transition:.5s}
.photo-wrap:hover{transform:rotate(0deg) translateY(-7px) scale(1.015)}
.photo{width:100%;height:460px;object-fit:cover;border-radius:22px;display:block}
.polaroid{background:#fff;padding:9px 9px 17px;border-radius:8px;box-shadow:0 18px 45px rgba(70,30,55,.16);transform:rotate(-2deg);transition:.5s}
.polaroid:nth-child(2){transform:rotate(2deg)}
.polaroid:nth-child(3){transform:rotate(-1deg)}
.polaroid:hover{transform:translateY(-12px) rotate(0deg)}
.polaroid img{width:100%;height:290px;object-fit:cover;border-radius:4px}
.caption{font-family:'Cormorant Garamond',serif;color:#6c4657;text-align:center;font-size:18px;padding-top:9px}

/* Memory constellation */
.memory-card{padding:25px;text-align:center;height:100%;transition:.5s}
.memory-card:hover{transform:translateY(-8px)}
.icon{font-size:2.4rem;margin-bottom:8px}
.memory-card h3{font-family:'DM Serif Display',serif;color:#a2486e;font-size:25px;margin:4px}
.memory-card p{color:#6d5060;line-height:1.7;font-size:14px}

/* Envelope */
.envelope{max-width:600px;margin:30px auto;padding:45px 30px;text-align:center;border-radius:28px;background:linear-gradient(145deg,#fff,#fff0f7);border:1px solid #f3c8d9;box-shadow:0 25px 70px rgba(165,68,111,.17)}
.envelope-icon{font-size:90px;animation:floatGift 2.5s ease-in-out infinite}
@keyframes floatGift{50%{transform:translateY(-12px) rotate(2deg)}}

/* Timeline */
.timeline{position:relative;max-width:850px;margin:auto}
.timeline:before{content:"";position:absolute;left:22px;top:0;bottom:0;width:2px;background:linear-gradient(#ffc0d5,#cdb8ef,#ffc0d5)}
.timeline-card{margin:18px 0 18px 55px;padding:22px 25px}
.timeline-dot{position:absolute;left:-47px;top:24px;width:17px;height:17px;background:#e85d8c;border:4px solid #fff;border-radius:50%;box-shadow:0 0 0 5px rgba(232,93,140,.15)}

/* Final */
.final-card{text-align:center;padding:55px 25px;overflow:hidden}
.big-heart{font-size:90px;display:inline-block;animation:heartbeat 1.5s ease-in-out infinite}
@keyframes heartbeat{0%,100%{transform:scale(1)}14%{transform:scale(1.15)}28%{transform:scale(1)}42%{transform:scale(1.1)}}
.shimmer{background:linear-gradient(90deg,#c94d79,#ff8aae,#9c78cc,#c94d79);background-size:300% auto;color:transparent;background-clip:text;-webkit-background-clip:text;animation:shimmer 4s linear infinite}
@keyframes shimmer{to{background-position:300% center}}

/* Streamlit buttons */
div.stButton>button{border:1px solid rgba(255,255,255,.85)!important;border-radius:999px!important;background:linear-gradient(100deg,#e65e8c,#d96a9a)!important;color:white!important;font-weight:700!important;min-height:48px;box-shadow:0 10px 28px rgba(213,79,127,.20)!important;transition:.25s!important}
div.stButton>button:hover{transform:translateY(-3px) scale(1.01)!important;box-shadow:0 15px 34px rgba(213,79,127,.28)!important}
.stProgress>div>div>div>div{background:linear-gradient(90deg,#e65e8c,#b67bd8)!important}

/* Hide Streamlit chrome */
#MainMenu{visibility:hidden} footer{visibility:hidden} header{visibility:hidden}
</style>

<div class="fx">
  <div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div>
  <span class="particle" style="left:4%;animation-duration:13s;animation-delay:-2s;font-size:22px;color:#e982a6">♥</span>
  <span class="particle" style="left:12%;animation-duration:17s;animation-delay:-9s;font-size:16px;color:#c79bdc">✦</span>
  <span class="particle" style="left:22%;animation-duration:15s;animation-delay:-4s;font-size:28px;color:#f0a0bb">♡</span>
  <span class="particle" style="left:34%;animation-duration:19s;animation-delay:-12s;font-size:18px;color:#d39bc0">✧</span>
  <span class="particle" style="left:47%;animation-duration:14s;animation-delay:-7s;font-size:24px;color:#e982a6">♥</span>
  <span class="particle" style="left:59%;animation-duration:18s;animation-delay:-3s;font-size:17px;color:#c79bdc">✦</span>
  <span class="particle" style="left:71%;animation-duration:16s;animation-delay:-11s;font-size:26px;color:#f0a0bb">♡</span>
  <span class="particle" style="left:84%;animation-duration:20s;animation-delay:-6s;font-size:20px;color:#d39bc0">✧</span>
  <span class="particle" style="left:94%;animation-duration:15s;animation-delay:-13s;font-size:25px;color:#e982a6">♥</span>
</div>
""", unsafe_allow_html=True)

# -------------------- Top navigation --------------------
nav = st.columns(5)
for col, label, target in zip(nav, ["🏠 Home", "🎞 Memories", "🌙 Our Things", "💌 Letter", "🎉 Finale"], ["intro","memories","things","letter","final"]):
    with col:
        if st.button(label, key=f"nav_{target}", use_container_width=True):
            go(target)

# ==================== INTRO ====================
if st.session_state.page == "intro":
    st.markdown("""
    <div class="hero">
      <div class="kicker">A PRIVATE LITTLE CORNER OF THE INTERNET</div>
      <div style="font-size:26px;margin:12px 0">🎀 ✨ 🌷 💗 🌷 ✨ 🎀</div>
      <div class="script">Happy Birthday</div>
      <div class="script small">Siddhi Jeeee 💗</div>
      <p class="subtitle">I made this tiny universe for one very special person.<br>Take a breath. Press the button. Let the surprise begin. ✨</p>
      <span class="pill">made with care</span><span class="pill">for someone irreplaceable</span><span class="pill">one-of-one</span>
    </div>
    """, unsafe_allow_html=True)

    if imgs:
        st.markdown('<div class="photo-wrap">' + safe_img(imgs[0], "photo") + '</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="glass card-pad center" style="margin-top:24px">
      <div class="icon">🌸</div>
      <div class="quote">&ldquo;Some people enter your life quietly… and somehow become one of the most beautiful parts of it.&rdquo;</div>
      <p class="body">Siddhi, before anything else, I want you to know that <b>I am genuinely blessed to have you in my life.</b> ❤️ You are more than just my best friend — you are someone incredibly special to me, someone I never want to take for granted.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💌 OPEN YOUR BIRTHDAY UNIVERSE", use_container_width=True, type="primary"):
        st.session_state.opened = True
        go("memories")

    if st.session_state.opened:
        st.success("✨ The surprise is officially open. Keep going… there is more waiting for you. 💗")

# ==================== MEMORIES ====================
elif st.session_state.page == "memories":
    st.markdown('<div class="hero"><div class="kicker">CHAPTER ONE</div><div class="section-title" style="margin-top:6px">Little Frames of Siddhi 📸</div><p class="subtitle">A few pictures. A thousand little feelings.</p></div>', unsafe_allow_html=True)

    if imgs:
        # Large feature image
        feature = imgs[st.session_state.memory % len(imgs)]
        st.markdown('<div class="photo-wrap">' + safe_img(feature, "photo") + '</div>', unsafe_allow_html=True)
        st.caption("✨ Every version of you deserves a place in this little story.")

        st.markdown('<div class="section-title">The Gallery ✨</div>', unsafe_allow_html=True)
        cols = st.columns(2)
        captions = [
            "That smile. That's the whole caption. 🌷",
            "A tiny frame from a very big collection of memories. 💗",
            "One of those pictures that just feels like you. ✨",
            "Proof that ordinary moments can become priceless. 🫶",
            "And yes… you looked this cute. 😂❤️",
        ]
        for i, img in enumerate(imgs):
            with cols[i % 2]:
                st.markdown('<div class="polaroid">' + safe_img(img, "") + f'<div class="caption">{captions[i % len(captions)]}</div></div>', unsafe_allow_html=True)
                st.write("")

        if st.button("✨ Show me another favourite", use_container_width=True):
            st.session_state.memory += 1
            st.rerun()

    st.markdown("<div class='glass card-pad center' style='margin-top:25px'><div class='quote'>&ldquo;The best memories aren't always photographed. Sometimes they are just two people talking until the night gets too quiet.&rdquo; 🌙</div></div>", unsafe_allow_html=True)

    if st.button("🌙 Go to the memories that cameras can't capture", use_container_width=True):
        go("things")

# ==================== OUR THINGS ====================
elif st.session_state.page == "things":
    st.markdown("<div class='hero'><div class='kicker'>CHAPTER TWO</div><div class='section-title' style='margin-top:6px'>The Little Things 🌙</div><p class='subtitle'>The moments that don't need a camera to be remembered.</p></div>", unsafe_allow_html=True)

    items = [
        ("🌙", "Late-night talks", "Those conversations that start with one random topic and somehow turn into everything — life, dreams, problems, nonsense and laughter."),
        ("💭", "Sharing everything", "Being able to share thoughts and feelings without worrying about being judged. That kind of comfort is rare, and I value it."),
        ("🫶", "Caring for you", "Looking out for you, checking in, wanting you to be okay — because your happiness genuinely matters to me."),
        ("😂", "The Jharkhandi accent", "Okay, this absolutely deserves its own chapter. 😂 Some things become inside jokes simply because they are too adorable to forget."),
    ]
    cols = st.columns(2)
    for i, (icon, title, text) in enumerate(items):
        with cols[i % 2]:
            st.markdown(f'<div class="memory-card"><div class="icon">{icon}</div><h3>{title}</h3><p>{text}</p></div>', unsafe_allow_html=True)
            st.write("")

    st.markdown('<div class="timeline"><div class="timeline-card"><div class="timeline-dot"></div><b>Then</b><p class="body">Two people talking, laughing, sharing random thoughts.</p></div><div class="timeline-card"><div class="timeline-dot"></div><b>Somewhere along the way</b><p class="body">Those little conversations started feeling important.</p></div><div class="timeline-card"><div class="timeline-dot"></div><b>Now</b><p class="body">I can honestly say you became much more than just a best friend. You became one of those rare people who feel irreplaceable. I am genuinely blessed to have you in my life. ❤️</p></div></div>', unsafe_allow_html=True)

    if st.button("💌 There is a letter waiting for you", use_container_width=True, type="primary"):
        go("letter")

# ==================== LETTER ====================
elif st.session_state.page == "letter":
    st.markdown('<div class="hero"><div class="big-heart">💗</div><div class="kicker">CHAPTER THREE</div><div class="section-title" style="margin-top:6px">A Letter for Siddhi</div><p class="subtitle">Read this slowly. I meant every word.</p></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="letter card-pad">
      <p class="quote"><b>Dear Siddhi jeeee,</b> 🌷</p>
      <p class="body">I don't think a website, a message, or even a thousand words can perfectly explain how much a person means to you. But I wanted to try anyway.</p>
      <p class="body">I am <b>genuinely blessed to have you in my life.</b> ❤️ You are more than just my best friend; you are someone deeply special to me, someone whose presence means more than I can put into words. And I hope you never forget that.</p>
      <p class="body">From our late-night talks to the times I have shared my thoughts and feelings with you, there is a kind of comfort in our friendship that I don't take for granted.</p>
      <p class="body">I love the little things too — caring about you, checking on you, laughing over random stuff, and of course your unforgettable <b>Jharkhandi accent</b> 😂❤️.</p>
      <p class="body">I hope this new year of your life brings you confidence, peace, beautiful people, exciting opportunities and every achievement you are working towards.</p>
      <p class="body">Please remember: <b>you are strong, you are brave, and you are capable of achieving anything you truly want.</b> ✨</p>
      <p class="body">When life feels difficult, don't let one bad chapter convince you that the whole story is bad. Keep going. Keep believing in yourself. You have so much ahead of you.</p>
      <p class="quote">Happy Birthday, Siddhi. 🎂💗<br>Thank you for being you.</p>
      <p class="quote" style="text-align:right">— Someone who will always care about you 🫶</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="envelope"><div class="envelope-icon">💌</div><h2 style="color:#a2486e;font-family:DM Serif Display,serif">One last secret…</h2><p class="body">The final page is not another message. It is the part I really want you to remember.</p></div>', unsafe_allow_html=True)

    if st.button("✨ OPEN THE FINAL REVEAL", use_container_width=True, type="primary"):
        st.session_state.final = True
        go("final")

# ==================== FINAL ====================
elif st.session_state.page == "final":
    if st.session_state.final:
        st.balloons()

    st.markdown("""
    <div class="final-card">
      <div class="confetti" style="font-size:30px;letter-spacing:14px">🎉 ✨ 🎊 💗 🎊 ✨ 🎉</div>
      <div class="big-heart">❤️</div>
      <div class="kicker">THE FINAL REVEAL</div>
      <div class="script shimmer">Siddhi Jeeee</div>
      <div class="script small">You are special. 💗</div>
      <p class="quote">Not because it's your birthday.<br>Because you are you.</p>
      <p class="body" style="max-width:720px;margin:20px auto">I hope whenever you look back at this little surprise, you remember one simple thing:</p>
      <div style="font-family:'DM Serif Display',serif;color:#d54f7f;font-size:clamp(1.8rem,5vw,3.2rem);line-height:1.2">✨ I AM BLESSED TO HAVE YOU IN MY LIFE. ✨</div>
      <p class="body" style="max-width:680px;margin:22px auto">Keep smiling. Keep dreaming. Keep being the wonderfully chaotic, caring, strong Siddhi I know. And please never stop believing in yourself. 🌷</p>
      <div class="pill">Happy Birthday, Siddhi Jeeee 🎂💗</div>
      <div class="pill">Always cheering for you 🌟</div>
      <div class="pill">Made especially for you 💌</div>
    </div>
    """, unsafe_allow_html=True)

    if imgs:
        st.markdown('<div class="section-title">A final little gallery 🌸</div>', unsafe_allow_html=True)
        cols = st.columns(len(imgs))
        for i, img in enumerate(imgs):
            with cols[i]:
                st.markdown('<div class="polaroid">' + safe_img(img, "") + '</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass card-pad center" style="margin-top:25px"><div class="quote">&ldquo;Some friendships are not loud. They simply become home.&rdquo; 🫶</div><p class="body">Thank you for becoming such a special part of my story, Siddhi. Some people are simply friends; you became so much more than that to me. ❤️</p></div>', unsafe_allow_html=True)

    if st.button("🔁 Experience it from the beginning", use_container_width=True):
        st.session_state.page = "intro"
        st.session_state.opened = False
        st.session_state.final = False
        st.session_state.memory = 0
        st.rerun()

# -------------------- Optional music --------------------
music = ASSETS / "birthday_music.mp3"
if music.exists():
    st.markdown('<div style="height:18px"></div>', unsafe_allow_html=True)
    st.audio(str(music), format="audio/mp3")
else:
    st.markdown('<p class="small center" style="margin-top:28px">🎵 Tip: add <b>birthday_music.mp3</b> inside <b>assets/</b> if you want background birthday music.</p>', unsafe_allow_html=True)
