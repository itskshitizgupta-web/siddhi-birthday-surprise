import streamlit as st
from pathlib import Path
import random
import html
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Siddhi Jeeee • A Little Universe",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE = Path(__file__).parent
ASSETS = BASE / "assets"

# -----------------------------
# Premium 3D / cinematic CSS
# -----------------------------
st.markdown(r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=DM+Serif+Display&family=Manrope:wght@400;500;600;700&display=swap');

:root{
  --pink:#ff7da8;
  --rose:#d94f82;
  --ink:#311b2b;
  --muted:#785768;
  --glass:rgba(255,255,255,.66);
}

html, body, [data-testid="stAppViewContainer"]{
  background:
    radial-gradient(circle at 15% 10%, rgba(255,160,200,.25), transparent 28%),
    radial-gradient(circle at 90% 25%, rgba(176,141,226,.22), transparent 30%),
    radial-gradient(circle at 45% 100%, rgba(255,220,235,.5), transparent 32%),
    linear-gradient(135deg,#fffaff 0%,#fff3f8 48%,#f6effa 100%);
}

[data-testid="stHeader"]{background:transparent;}
[data-testid="stToolbar"]{display:none;}
.block-container{max-width:1180px;padding:1rem 1.2rem 4rem;}

.hero{text-align:center; padding:1.2rem 0 .5rem;}
.kicker{font-family:Manrope,sans-serif;font-size:11px;letter-spacing:4px;font-weight:700;color:#b65c82;}
.hero h1{font-family:'DM Serif Display',serif!important;color:#c94476!important;
font-size:clamp(40px,7vw,76px)!important;line-height:1.02!important;margin:.25rem 0!important;
text-shadow:0 8px 30px rgba(217,79,130,.16);}
.hero p{font-family:Manrope,sans-serif;color:var(--muted);font-size:14px;}

.glass{
 background:linear-gradient(135deg,rgba(255,255,255,.78),rgba(255,255,255,.42));
 border:1px solid rgba(255,255,255,.9);
 border-radius:32px;padding:26px;
 box-shadow:0 24px 70px rgba(91,35,69,.12), inset 0 1px 0 rgba(255,255,255,.9);
 backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);
 margin:18px 0;
}

.section-title{font-family:'DM Serif Display',serif;color:#7e3656;font-size:34px;text-align:center;margin:6px 0 4px;}
.section-sub{font-family:Manrope,sans-serif;color:#896575;text-align:center;font-size:13px;margin-bottom:20px;}

.photo-card{
 border-radius:24px;padding:7px;background:linear-gradient(145deg,#fff,#f5dce8);
 box-shadow:0 16px 35px rgba(90,35,65,.15);
 transform:perspective(900px) rotateX(1deg);
 transition:transform .5s ease, box-shadow .5s ease;
}
.photo-card:hover{transform:perspective(900px) rotateX(0) rotateY(-5deg) translateY(-8px) scale(1.025);
box-shadow:0 30px 55px rgba(90,35,65,.22);}
.photo-card img{border-radius:19px;}

.quote{
 font-family:'Cormorant Garamond',serif;color:#6c4054;text-align:center;
 font-size:clamp(22px,3vw,32px);line-height:1.3;
}
.highlight{
 font-family:'DM Serif Display',serif;color:#d84e80;text-align:center;
 font-size:clamp(27px,4vw,45px);line-height:1.12;
 text-shadow:0 0 28px rgba(255,108,157,.25);
}

.memory{
 background:rgba(255,248,252,.72);border:1px solid #f3d5e2;border-radius:22px;
 padding:18px 20px;margin:10px 0;color:#664656;font-family:Manrope,sans-serif;
 box-shadow:0 10px 25px rgba(100,40,70,.06);
}
.memory b{color:#d05280;}

div.stButton>button{
 width:100%;border:0;border-radius:999px!important;padding:14px 20px!important;
 background:linear-gradient(90deg,#ec6b9d,#c94e7b)!important;color:white!important;
 font-family:Manrope,sans-serif!important;font-weight:800!important;
 box-shadow:0 12px 30px rgba(201,78,123,.26)!important;
 transition:transform .25s ease,box-shadow .25s ease!important;
}
div.stButton>button:hover{transform:translateY(-3px) scale(1.01);box-shadow:0 18px 35px rgba(201,78,123,.35)!important;}

.stImage img{border-radius:22px;}

@keyframes drift{
  0%{transform:translate3d(0,0,0) rotate(0deg);}
  50%{transform:translate3d(20px,-34px,0) rotate(8deg);}
  100%{transform:translate3d(0,-70px,0) rotate(0deg);}
}
@keyframes pulse3d{
  0%,100%{transform:scale(1) rotateX(0) rotateY(0);}
  50%{transform:scale(1.09) rotateX(8deg) rotateY(-8deg);}
}
@keyframes shimmer{
  0%{background-position:-250% 0;}
  100%{background-position:250% 0;}
}
.shimmer{
 background:linear-gradient(100deg,#d94f82 25%,#fff 40%,#d94f82 55%);
 background-size:250% auto;-webkit-background-clip:text;background-clip:text;color:transparent;
 animation:shimmer 4s linear infinite;
}

.floating{
 position:fixed;left:0;top:0;width:100%;height:100%;pointer-events:none;z-index:0;overflow:hidden;
}
.floating span{
 position:absolute;bottom:-80px;font-size:20px;opacity:.42;
 animation:drift linear infinite;
 filter:drop-shadow(0 7px 12px rgba(210,65,120,.18));
}
.floating span:nth-child(1){left:4%;animation-duration:12s;animation-delay:-2s;}
.floating span:nth-child(2){left:12%;animation-duration:16s;animation-delay:-8s;}
.floating span:nth-child(3){left:23%;animation-duration:11s;animation-delay:-5s;}
.floating span:nth-child(4){left:35%;animation-duration:18s;animation-delay:-12s;}
.floating span:nth-child(5){left:48%;animation-duration:13s;animation-delay:-3s;}
.floating span:nth-child(6){left:61%;animation-duration:17s;animation-delay:-10s;}
.floating span:nth-child(7){left:74%;animation-duration:12s;animation-delay:-7s;}
.floating span:nth-child(8){left:86%;animation-duration:19s;animation-delay:-15s;}
.floating span:nth-child(9){left:94%;animation-duration:14s;animation-delay:-4s;}

@media(max-width:700px){
 .glass{padding:18px;border-radius:25px;}
 .section-title{font-size:28px;}
 .hero h1{font-size:44px!important;}
}
</style>

<div class="floating">
<span>♥</span><span>✦</span><span>♡</span><span>✧</span><span>♥</span>
<span>•</span><span>♡</span><span>✦</span><span>♥</span>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 3D cinematic opening scene
# -----------------------------
components.html(r"""
<!doctype html>
<html>
<head>
<style>
*{box-sizing:border-box}
body{margin:0;background:transparent;font-family:Arial,sans-serif}
.scene{height:270px;position:relative;display:flex;align-items:center;justify-content:center;
perspective:1000px;overflow:hidden;border-radius:34px;
background:radial-gradient(circle at 50% 48%,rgba(255,154,194,.35),transparent 25%),
linear-gradient(135deg,rgba(255,255,255,.65),rgba(255,232,242,.35));}
.orb{position:absolute;border-radius:50%;filter:blur(1px);opacity:.55;
box-shadow:inset -18px -18px 30px rgba(160,70,120,.12),inset 12px 12px 28px rgba(255,255,255,.75),0 20px 50px rgba(120,50,90,.14);}
.o1{width:85px;height:85px;left:8%;top:30%;background:radial-gradient(circle at 30% 25%,#fff,#ffc1d8 42%,#df7ea8 100%);animation:float 6s ease-in-out infinite;}
.o2{width:55px;height:55px;right:12%;top:18%;background:radial-gradient(circle at 30% 25%,#fff,#d8baf0 45%,#a886c5 100%);animation:float 8s ease-in-out infinite reverse;}
.o3{width:32px;height:32px;right:25%;bottom:18%;background:radial-gradient(circle at 30% 25%,#fff,#ffd9e7 45%,#e89bb9);animation:float 5s ease-in-out infinite;}
.heart{width:95px;height:95px;position:relative;transform:rotate(-45deg);
background:linear-gradient(145deg,#ffb2ca,#d84d80 65%,#a92f60);
border-radius:18px 8px 18px 8px;animation:heart 2.7s ease-in-out infinite;
box-shadow:18px 24px 35px rgba(120,35,75,.25),inset 12px 12px 20px rgba(255,255,255,.32),inset -14px -14px 20px rgba(90,20,55,.18);}
.heart:before,.heart:after{content:"";position:absolute;width:95px;height:95px;border-radius:50%;
background:inherit;box-shadow:inset 12px 12px 20px rgba(255,255,255,.32),inset -14px -14px 20px rgba(90,20,55,.18);}
.heart:before{top:-47px;left:0}.heart:after{left:47px;top:0}
.spark{position:absolute;color:#fff;font-size:20px;text-shadow:0 0 15px #ff76a8;animation:twinkle 2s ease-in-out infinite;}
.s1{left:31%;top:25%}.s2{right:30%;top:62%;animation-delay:.7s}.s3{left:24%;bottom:18%;animation-delay:1.1s}
.caption{position:absolute;bottom:22px;color:#7a4d61;font-weight:700;letter-spacing:2px;font-size:11px;text-transform:uppercase}
@keyframes heart{0%,100%{transform:rotate(-45deg) scale(1) translateZ(0)}50%{transform:rotate(-41deg) scale(1.12) translateZ(35px)}}
@keyframes float{0%,100%{transform:translateY(0) translateZ(0)}50%{transform:translateY(-22px) translateZ(30px)}}
@keyframes twinkle{0%,100%{opacity:.2;transform:scale(.7)}50%{opacity:1;transform:scale(1.35)}}
</style>
</head>
<body>
<div class="scene">
<div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div>
<div class="spark s1">✦</div><div class="spark s2">✧</div><div class="spark s3">✦</div>
<div class="heart"></div>
<div class="caption">A tiny universe made just for Siddhi Jeeee ✨</div>
</div>
</body>
</html>
""", height=290, scrolling=False)

st.markdown("""
<div class="hero">
<div class="kicker">THIS ONE IS DIFFERENT</div>
<h1 class="shimmer">Happy Birthday, Siddhi Jeeee 💗</h1>
<p>Not just a birthday page. A tiny digital universe made for someone who means much more than words can explain.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Photo gallery
# -----------------------------
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.markdown('<div class="section-title">✨ A Few Little Glimpses</div><div class="section-sub">Every picture holds a different version of the person who became so special.</div>', unsafe_allow_html=True)

cols = st.columns(4, gap="small")
for i, col in enumerate(cols, 1):
    with col:
        st.markdown('<div class="photo-card">', unsafe_allow_html=True)
        st.image(str(ASSETS / f"siddhi_0{i}.jpg"), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# The "more than best friend" letter
# -----------------------------
st.markdown("""
<div class="glass">
<div class="quote">
“Siddhi jeeee… some people enter your life as friends,
and somewhere along the way, they quietly become something much more.”
</div>
<br>
<div class="quote">
You're not just my best friend. You're one of those rare people
with whom I can share the thoughts I keep inside, talk for hours at night,
and simply be myself.
</div>
<br>
<div class="quote">
From our late-night conversations 🌙, to sharing my thoughts and feelings,
to caring about you, and obviously surviving your legendary
<strong>Jharkhandi accent 😂</strong> — all these little things mean more to me
than I probably say out loud.
</div>
<br>
<div class="highlight">I AM GENUINELY BLESSED TO HAVE YOU. ❤️</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Memory cards
# -----------------------------
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🌙 The Little Things</div><div class="section-sub">The memories that look small, but somehow mean everything.</div>', unsafe_allow_html=True)

memory_cols = st.columns(2, gap="medium")
memories = [
    ("🌙 Late-night talks", "Those conversations where “just 5 minutes” somehow turned into hours."),
    ("💭 No-filter conversations", "Being able to share thoughts and feelings without pretending to be okay."),
    ("🫶 Caring about you", "Wanting you to be happy, safe, smiling and doing well genuinely matters to me."),
    ("😂 That Jharkhandi accent", "Yes, Siddhi jeeee, this absolutely deserved its own memory card. 😂❤️"),
]
for col, (title, text) in zip(memory_cols * 2, memories):
    with col:
        st.markdown(f'<div class="memory"><b>{title}</b><br>{text}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Bitmoji-style sticker universe
# -----------------------------
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🎀 Siddhi in Sticker Universe</div><div class="section-sub">Cute little Bitmoji-style moments made specially for this surprise.</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;perspective:1200px;">
  <div style="
    display:inline-block;max-width:900px;width:100%;
    padding:12px;border-radius:30px;
    background:linear-gradient(145deg,rgba(255,255,255,.9),rgba(255,232,242,.7));
    box-shadow:0 25px 70px rgba(93,35,70,.16);
    transform:rotateX(2deg);
  ">
""", unsafe_allow_html=True)
st.image(str(ASSETS / "siddhi_bitmoji_stickers.png"), use_container_width=True)
st.markdown("</div></div>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Birthday video
# -----------------------------
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🎬 A Little Video For You</div><div class="section-sub">Because some memories deserve a screen of their own.</div>', unsafe_allow_html=True)

video = ASSETS / "birthday_video.mp4"
if video.exists():
    st.video(str(video))
else:
    st.info("The birthday video file is not present yet.")

st.markdown("""
<div class="quote">
“Just one more little reminder that you are much more than a title,
and that having you in my life is something I will always be grateful for. ❤️”
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Interactive final reveal
# -----------------------------
if "reveal" not in st.session_state:
    st.session_state.reveal = False

st.markdown('<div class="glass">', unsafe_allow_html=True)
st.markdown('<div class="section-title">💌 One Last Secret</div>', unsafe_allow_html=True)

if not st.session_state.reveal:
    st.markdown('<div class="section-sub">There is one thing I wanted to say without hiding behind a simple “Happy Birthday”.</div>', unsafe_allow_html=True)
    if st.button("🔐 UNLOCK THE MESSAGE", key="unlock"):
        st.session_state.reveal = True
        st.rerun()
else:
    st.balloons()
    components.html(r"""
    <!doctype html><html><head><style>
    body{margin:0;background:transparent;font-family:Georgia,serif}
    .wrap{height:280px;display:flex;align-items:center;justify-content:center;perspective:900px}
    .card{width:min(680px,92vw);padding:38px 24px;border-radius:30px;text-align:center;
    background:linear-gradient(145deg,rgba(255,255,255,.96),rgba(255,237,245,.88));
    border:1px solid #fff;box-shadow:0 30px 80px rgba(88,30,65,.2),inset 0 1px 0 #fff;
    animation:enter 1.2s cubic-bezier(.2,.8,.2,1) both}
    .heart{font-size:55px;filter:drop-shadow(0 10px 18px rgba(210,55,115,.3));animation:p 1.8s infinite}
    h2{color:#cf4d7c;font-size:30px;margin:10px}
    p{color:#664455;line-height:1.75;font-size:15px}
    .big{color:#d94f82;font-size:25px;font-weight:bold}
    @keyframes enter{from{opacity:0;transform:rotateX(25deg) translateY(40px) scale(.92)}to{opacity:1;transform:none}}
    @keyframes p{0%,100%{transform:scale(1)}50%{transform:scale(1.15)}}
    </style></head><body>
    <div class="wrap"><div class="card">
      <div class="heart">❤️</div>
      <h2>Siddhi Jeeee…</h2>
      <p>
      I don't know if there is a perfect word for what you are to me.<br>
      I only know that you're <b>much more than just my best friend.</b><br><br>
      You're someone I deeply value, someone I can open my heart to,
      and someone whose presence has become a beautiful part of my life.
      </p>
      <div class="big">I'm blessed to have you. ✨</div>
      <p>Happy Birthday, Siddhi. Keep being the beautiful, crazy, caring you. 🌷</p>
    </div></div>
    </body></html>
    """, height=300, scrolling=False)

    if st.button("🌸 Replay the surprise", key="replay"):
        st.session_state.reveal = False
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;padding:20px 0;color:#9a7182;font-family:Manrope,sans-serif;font-size:12px;">
Made with a ridiculous amount of care for Siddhi Jeeee 💗<br>
Some people are friends. Some become family. Some become something words can't properly describe.
</div>
""", unsafe_allow_html=True)
