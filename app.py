import base64
import os
import random

import streamlit as st

st.set_page_config(
    page_title="Ahmad Asyaddad | Portfolio",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def h(s: str) -> str:
    """Rapatkan HTML jadi satu baris agar Markdown tidak salah baca indentasi."""
    return "".join(line.strip() for line in s.strip().splitlines())


def star_shadows(n: int, color: str, seed: int) -> str:
    rnd = random.Random(seed)
    return ",".join(f"{rnd.randint(0, 2000)}px {rnd.randint(0, 2000)}px {color}" for _ in range(n))


# =========================
# DATA (edit di sini)
# =========================
PHOTO_ORIGINAL = "foto.png"            # foto asli Anda
PHOTO_CUTOUT = "foto_transparan.png"   # hasil tanpa background (dibuat otomatis / manual)

BIODATA = [
    ("Nama", "Ahmad Asyaddad"),
    ("NIM", "26051204050"),
    ("Asal daerah", "Surabaya, Jawa Timur"),
    ("Pendidikan", "SMK Rajasa Surabaya, 2023 sampai 2026"),
    ("Hobi", "Renang, badminton, healing"),
]

SKILLS = [
    ("Python", "Core & logika", "#ff8a5b"),
    ("C / C++", "Algoritma", "#b9a8ff"),
    ("Flask", "Backend web", "#3ee0c5"),
    ("Streamlit", "Aplikasi data", "#7cc4ff"),
]

PROJECTS = [
    ("📊 Sistem Absensi INF26B", "Python • Streamlit", "#ff8a5b",
     "Antarmuka manajemen presensi kelas yang efisien, modern, dan berbasis data interaktif."),
]

CONTACTS = [
    ("WhatsApp", "0813-3041-9416", "https://wa.me/6281330419416"),
    ("Instagram", "@ahmad_asyaddad", "https://instagram.com/ahmad_asyaddad"),
    ("TikTok", "asyad_shop_official", "https://www.tiktok.com/@asyad_shop_official"),
    ("LinkedIn", "AHMAD ASYADDAD", "https://linkedin.com/in/AHMAD-ASYADDAD"),
]

# Animasi tetap jalan walau Windows/HP Anda memakai mode "kurangi gerakan".
# Ubah ke True jika ingin menghormati pengaturan itu (animasi dimatikan).
RESPECT_REDUCED_MOTION = False
REDUCED_CSS = """@media (prefers-reduced-motion: reduce){
  .layer,.meteor,.name,.badge i,.lan,.swing,.sway,.idcard::after,.track,.ph,.ga,.gb,.holo,.scanb,.bar{animation:none !important;}
}"""

# =========================
# CSS
# =========================
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700&family=Outfit:wght@300;400;600&family=Great+Vibes&display=swap');
:root{--void:#04040c; --nebula:#5b3df5; --aurora:#3ee0c5; --star:#eef2ff; --ember:#ff8a5b; --dust:#9aa3c7;
  --line:rgba(154,163,199,.16); --panel:rgba(14,14,34,.58);}
.stApp{
  background:
    radial-gradient(ellipse 60% 50% at 15% 10%, rgba(91,61,245,.28), transparent 70%),
    radial-gradient(ellipse 50% 45% at 90% 35%, rgba(62,224,197,.14), transparent 70%),
    var(--void);
  color:var(--star); font-family:'Outfit',sans-serif;}
#MainMenu, footer, header{visibility:hidden;}
.block-container{position:relative; z-index:2; max-width:1100px; padding-top:3rem;}

/* Bintang + bintang jatuh */
.sky{position:fixed; inset:0; z-index:0; pointer-events:none; overflow:hidden;}
.layer{position:absolute; top:0; left:0; border-radius:50%;}
.layer::after{content:""; position:absolute; top:2000px; left:0; width:inherit; height:inherit; border-radius:50%; box-shadow:inherit;}
.l1{width:1px;height:1px; box-shadow:__S1__; animation:drift 160s linear infinite;}
.l2{width:2px;height:2px; box-shadow:__S2__; animation:drift 90s linear infinite;}
.l3{width:3px;height:3px; box-shadow:__S3__; animation:drift 50s linear infinite, twinkle 4s ease-in-out infinite;}
@keyframes drift{to{transform:translateY(-2000px);}}
@keyframes twinkle{50%{opacity:.35;}}
.meteor{position:absolute; width:160px; height:2px; opacity:0; transform:rotate(-35deg);
  background:linear-gradient(90deg, rgba(255,255,255,0), #fff); animation:shoot 10s ease-in infinite;}
.m1{top:12%; left:78%; animation-delay:1s;}
.m2{top:30%; left:96%; animation-delay:6s; animation-duration:12s;}
@keyframes shoot{0%{opacity:0; translate:0 0;} 4%{opacity:1;} 14%,100%{opacity:0; translate:-520px 360px;}}

/* Hero */
.badge{display:inline-flex; align-items:center; gap:10px; padding:6px 16px; border-radius:999px; font-size:14px;
  color:var(--aurora); border:1px solid rgba(62,224,197,.35); background:rgba(62,224,197,.06);}
.badge i{width:8px; height:8px; border-radius:50%; background:var(--aurora); animation:pulse 2s infinite;}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(62,224,197,.7);} 70%,100%{box-shadow:0 0 0 10px rgba(62,224,197,0);}}
.name{font-family:'Unbounded',sans-serif; font-weight:700; line-height:1.05; margin:18px 0 8px;
  font-size:clamp(2.6rem,6.4vw,5rem);
  background:linear-gradient(100deg,#fff 0%,var(--aurora) 35%,#b9a8ff 70%,#fff 100%); background-size:250% auto;
  -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; animation:shine 8s linear infinite;}
@keyframes shine{to{background-position:250% center;}}
.role{font-size:1.25rem; color:var(--dust); margin-bottom:18px;}
.lead{color:var(--dust); font-weight:300; line-height:1.75; max-width:520px; font-size:1.05rem;}

/* Kartu ID bertali: tali jatuh dari atas, memantul, lalu berayun */
.lan{width:min(290px,100%); margin:0 auto; animation:drop 1.6s .5s both;}
@keyframes drop{
  0%{transform:translateY(-135%); animation-timing-function:cubic-bezier(.5,0,1,.65);}
  45%{transform:translateY(0); animation-timing-function:cubic-bezier(0,.45,.5,1);}
  62%{transform:translateY(-7%); animation-timing-function:cubic-bezier(.5,0,1,.65);}
  78%{transform:translateY(0); animation-timing-function:cubic-bezier(0,.45,.5,1);}
  88%{transform:translateY(-1.5%); animation-timing-function:ease-in;}
  100%{transform:translateY(0);}}
.swing{transform-origin:50% 0; animation:swing 3.8s ease-in-out 1.1s both;}
@keyframes swing{0%{transform:rotate(0);} 12%{transform:rotate(8deg);} 28%{transform:rotate(-6deg);}
  44%{transform:rotate(4deg);} 60%{transform:rotate(-2.5deg);} 76%{transform:rotate(1.4deg);} 100%{transform:rotate(0);}}
.sway{transform-origin:50% 0; animation:sway 7s ease-in-out 4.9s infinite alternate both;}
@keyframes sway{from{transform:rotate(-1.4deg);} to{transform:rotate(1.4deg);}}
.strap{width:38px; height:190px; margin:0 auto; position:relative; overflow:hidden; background:#09090d;
  border-inline:1px solid rgba(255,255,255,.1);
  -webkit-mask-image:linear-gradient(to bottom,transparent,#000 30%); mask-image:linear-gradient(to bottom,transparent,#000 30%);}
.strap span{position:absolute; left:50%; top:46px; transform:translateX(-50%); writing-mode:vertical-rl;
  font:600 10px/1 'Outfit',sans-serif; letter-spacing:2.5px; color:#fff; white-space:nowrap; opacity:.92;}
.clip{position:relative; z-index:3; width:26px; height:36px; margin:-4px auto 0; border-radius:7px 7px 10px 10px;
  background:linear-gradient(90deg,#1b1b22,#3a3a46 50%,#1b1b22); box-shadow:0 4px 10px rgba(0,0,0,.6);}
.clip::after{content:""; position:absolute; left:50%; top:8px; width:10px; height:10px; margin-left:-5px; border-radius:50%;
  border:2px solid #0a0a0e; background:#04040c;}
.idcard{position:relative; margin-top:-14px; aspect-ratio:3/4; border-radius:16px; overflow:hidden;
  background:linear-gradient(180deg,#1b9ab8 0%,#0f4f82 46%,#071a3c 100%);
  border:1px solid rgba(255,255,255,.2); box-shadow:0 26px 50px rgba(0,0,0,.65), 0 0 34px rgba(62,224,197,.22);}
/* Animasi avatar 10 detik (berulang): pindai > hologram > berwarna penuh > zoom > glitch > ulang */
.ph,.ga,.gb{position:absolute; inset:0; background-image:var(--ph); background-size:cover; background-position:50% 12%;}
.ph{z-index:0; animation:avatar 10s 2.2s infinite both;}
.ga,.gb{z-index:1; opacity:0; mix-blend-mode:screen;}
.ga{filter:hue-rotate(90deg) saturate(3); animation:gA 10s 2.2s infinite both;}
.gb{filter:hue-rotate(-90deg) saturate(3); animation:gB 10s 2.2s infinite both;}
.holo{position:absolute; inset:0; z-index:1; background:#19e3ff; mix-blend-mode:color; opacity:0; animation:holo 10s 2.2s infinite both;}
.scanb{position:absolute; left:0; right:0; top:0; height:3px; z-index:3; background:#9ff3e4; opacity:0;
  box-shadow:0 0 18px 6px rgba(62,224,197,.8); animation:beam 10s 2.2s infinite both;}
.bar{position:absolute; left:0; bottom:0; height:3px; width:100%; z-index:5; background:linear-gradient(90deg,#3ee0c5,#7c5cff);
  transform-origin:0 50%; animation:fill 10s linear 2.2s infinite both;}
@keyframes avatar{
  0%{opacity:0; clip-path:inset(0 0 100% 0); transform:scale(1.14) translateY(2%); filter:brightness(0) contrast(1.4) saturate(0);}
  8%{opacity:1; clip-path:inset(0 0 0 0); transform:scale(1.12) translateY(1.5%); filter:brightness(1.7) contrast(1.2) saturate(0);}
  14%{transform:scale(1.1); filter:brightness(1.1) contrast(1.25) saturate(0);}
  28%{transform:scale(1.08); filter:brightness(1.15) contrast(1.2) saturate(0);}
  38%{transform:scale(1.04); filter:brightness(1) contrast(1) saturate(1);}
  62%{transform:scale(1.12) translate(0,-1.5%); filter:brightness(1.03) contrast(1.05) saturate(1.1);}
  78%{transform:scale(1.1) translate(-1.5%,-1%); filter:brightness(1) contrast(1) saturate(1);}
  88%{transform:scale(1.06) translate(0,0); filter:brightness(1) contrast(1) saturate(1);}
  95%{opacity:1; clip-path:inset(0 0 0 0); transform:scale(1.1); filter:brightness(2.2) contrast(1.2) saturate(0);}
  100%{opacity:0; clip-path:inset(0 0 100% 0); transform:scale(1.14) translateY(2%); filter:brightness(0) contrast(1.4) saturate(0);}}
@keyframes holo{0%{opacity:0;} 8%{opacity:.9;} 28%{opacity:.85;} 38%{opacity:0;} 88%{opacity:0;} 95%{opacity:.9;} 100%{opacity:.9;}}
@keyframes beam{0%{top:0; opacity:1;} 8%{top:100%; opacity:1;} 9%{top:100%; opacity:0;} 100%{top:100%; opacity:0;}}
@keyframes gA{0%,11%{opacity:0; transform:translateX(0);} 12%{opacity:.7; transform:translateX(-7px);} 13%{opacity:0;}
  55%{opacity:0;} 56%{opacity:.6; transform:translateX(5px);} 57%{opacity:0;}
  93%{opacity:0;} 94%{opacity:.7; transform:translateX(-8px);} 96%{opacity:.7; transform:translateX(6px);} 97%,100%{opacity:0;}}
@keyframes gB{0%,11%{opacity:0; transform:translateX(0);} 12%{opacity:.7; transform:translateX(7px);} 13%{opacity:0;}
  55%{opacity:0;} 56%{opacity:.6; transform:translateX(-5px);} 57%{opacity:0;}
  93%{opacity:0;} 94%{opacity:.7; transform:translateX(8px);} 96%{opacity:.7; transform:translateX(-6px);} 97%,100%{opacity:0;}}
@keyframes fill{from{transform:scaleX(0);} to{transform:scaleX(1);}}
.idcard .astro{position:absolute; inset:0 0 30% 0; display:flex; align-items:center; justify-content:center; font-size:120px;}
.idcard::before{content:""; position:absolute; inset:auto 0 0 0; height:58%; z-index:1;
  background:linear-gradient(to bottom,transparent,rgba(4,16,44,.92) 70%);}
.idcard::after{content:""; position:absolute; top:-20%; bottom:-20%; width:40%; left:-60%; z-index:3; transform:skewX(-18deg);
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.22),transparent); animation:sheen 6s ease-in-out 3s infinite;}
@keyframes sheen{0%{left:-60%;} 28%,100%{left:130%;}}
.slot{position:absolute; top:12px; left:50%; width:48px; height:9px; margin-left:-24px; border-radius:6px; z-index:4;
  background:#03030a; box-shadow:inset 0 1px 3px #000;}
.idcard .tag{position:absolute; top:30px; left:16px; z-index:2; font:600 11px 'Outfit',sans-serif; letter-spacing:2px; color:rgba(255,255,255,.85);}
.idcard .info{position:absolute; left:18px; right:16px; bottom:16px; z-index:2;}
.idcard .nm{font-family:'Great Vibes',cursive; font-size:3.1rem; line-height:1; color:#fff; text-shadow:0 2px 14px rgba(0,0,0,.5);}
.idcard .un{font:600 9.5px/1.5 'Outfit',sans-serif; letter-spacing:1.6px; color:rgba(255,255,255,.85); margin-top:4px;}

/* Marquee teknologi */
.marq{overflow:hidden; margin-top:70px; padding:14px 0; border-block:1px solid var(--line);
  -webkit-mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent); mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);}
.track{display:flex; width:max-content; animation:marq 30s linear infinite;}
.track span{font-family:'Unbounded',sans-serif; font-size:1.05rem; color:var(--dust); white-space:nowrap;}
.track span::after{content:"✦"; margin:0 44px; color:var(--aurora);}
@keyframes marq{to{transform:translateX(-50%);}}

/* Bagian lain */
.sec{display:flex; align-items:center; gap:18px; font-family:'Unbounded',sans-serif; font-weight:500; font-size:1.6rem; margin:90px 0 28px;}
.sec::after{content:""; flex:1; height:1px; background:linear-gradient(90deg, rgba(62,224,197,.45), transparent);}
.card{height:100%; padding:22px 24px; border-radius:16px; background:var(--panel); backdrop-filter:blur(12px);
  border:1px solid var(--line); transition:border-color .3s, transform .3s;}
.card:hover{border-color:rgba(62,224,197,.5); transform:translateY(-4px);}
.card h3{margin:0 0 8px; font-size:1.2rem; color:var(--star);}
.card p{margin:0; color:var(--dust); font-weight:300; line-height:1.7; font-size:.98rem;}
.card .tech{font-size:13px; margin-bottom:8px;}
.bd{display:grid; grid-template-columns:repeat(2,1fr); gap:0 48px; padding:8px 28px; border-radius:18px;
  background:var(--panel); backdrop-filter:blur(12px); border:1px solid var(--line);}
.bd div{display:flex; justify-content:space-between; gap:16px; padding:15px 0; border-bottom:1px solid var(--line);}
.bd div:last-child{border-bottom:0;}
.bd div:nth-child(odd):last-child{grid-column:1/-1;}
.bd span{color:var(--dust); font-weight:300;}
.bd b{text-align:right;}
.chips{display:flex; flex-wrap:wrap; gap:14px;}
.chip{display:flex; align-items:center; gap:12px; padding:14px 24px; border-radius:999px; background:var(--panel);
  border:1px solid var(--line); transition:box-shadow .3s, border-color .3s;}
.chip:hover{border-color:rgba(62,224,197,.5); box-shadow:0 0 24px rgba(62,224,197,.2);}
.chip i{width:10px; height:10px; border-radius:50%;}
.chip b{font-size:1.1rem;} .chip span{color:var(--dust); font-size:14px;}
.contact{display:block; text-align:center; padding:18px 10px; border-radius:16px; background:var(--panel);
  border:1px solid var(--line); color:var(--aurora); text-decoration:none; font-weight:600; transition:border-color .25s, box-shadow .25s;}
.contact:hover{border-color:var(--aurora); box-shadow:0 0 24px rgba(62,224,197,.25); color:var(--aurora);}
.contact small{display:block; color:var(--dust); font-weight:300; margin-bottom:2px;}
.mail{display:block; text-align:center; margin-top:26px; color:#b9a8ff; font-size:1.1rem; font-weight:600; text-decoration:none;}
.foot{text-align:center; color:#5d6488; font-size:14px; margin-top:60px; padding-bottom:30px;}
@media (max-width:700px){.bd{grid-template-columns:1fr;}}

__REDUCED__
</style>
"""
CSS = (CSS.replace("__REDUCED__", REDUCED_CSS if RESPECT_REDUCED_MOTION else "")
          .replace("__S1__", star_shadows(500, "#cfd6ff", 1))
          .replace("__S2__", star_shadows(160, "#ffffff", 2))
          .replace("__S3__", star_shadows(45, "#9ff3e4", 3)))
st.markdown(CSS, unsafe_allow_html=True)
st.markdown(h("""
<div class="sky"><div class="layer l1"></div><div class="layer l2"></div><div class="layer l3"></div>
<div class="meteor m1"></div><div class="meteor m2"></div></div>
"""), unsafe_allow_html=True)


# =========================
# FOTO (hapus background otomatis jika rembg terpasang)
# =========================
@st.cache_data(show_spinner="Menyiapkan foto...")
def load_photo():
    """Kembalikan (bytes, mime, is_cutout)."""
    if os.path.exists(PHOTO_CUTOUT):
        return open(PHOTO_CUTOUT, "rb").read(), "image/png", True
    for name in (PHOTO_ORIGINAL, "foto.jpg", "foto.jpeg"):
        if os.path.exists(name):
            data = open(name, "rb").read()
            mime = "image/png" if name.endswith("png") else "image/jpeg"
            try:  # butuh: pip install "rembg[cpu]"
                from rembg import remove

                data = remove(data)
                open(PHOTO_CUTOUT, "wb").write(data)
                return data, "image/png", True
            except Exception:
                return data, mime, False
    return None


photo = load_photo()
src = f"data:{photo[1]};base64,{base64.b64encode(photo[0]).decode()}" if photo else None

if src:
    face = '<div class="ph"></div><div class="ga"></div><div class="gb"></div><div class="holo"></div>'
    card_style = f' style="--ph:url(\'{src}\')"'
else:
    face, card_style = '<div class="astro">🧑‍🚀</div>', ""
visual = f"""
<div class="lan"><div class="swing"><div class="sway">
<div class="strap"><span>AHMAD ASYADDAD</span></div>
<div class="clip"></div>
<div class="idcard"{card_style}>{face}<i class="slot"></i><i class="scanb"></i><i class="bar"></i>
<div class="tag">ANGKATAN 2026</div>
<div class="info"><div class="nm">Ahmad</div>
<div class="un">UNIVERSITAS NEGERI SURABAYA<br>S1 TEKNIK INFORMATIKA</div></div></div>
</div></div></div>"""

# =========================
# HERO
# =========================
c1, c2 = st.columns([3, 2], gap="large", vertical_alignment="center")
with c1:
    st.markdown(h("""
<div class="badge"><i></i>Tersedia untuk kolaborasi</div>
<div class="name">Ahmad Asyaddad</div>
<div class="role">Mahasiswa S1 Teknik Informatika · Web Developer</div>
<p class="lead">Mahasiswa angkatan 2026 di Universitas Negeri Surabaya (UNESA) yang menargetkan lulus dalam 3,5 tahun.
Berfokus pada pengembangan perangkat lunak dengan Python dan senang memecahkan masalah logika.</p>
"""), unsafe_allow_html=True)
with c2:
    st.markdown(h(visual), unsafe_allow_html=True)

names = [t for t, _, _ in SKILLS]
st.markdown(h('<div class="marq"><div class="track">' + "".join(f"<span>{n}</span>" for n in names * 6) + "</div></div>"),
            unsafe_allow_html=True)

# =========================
# BIODATA
# =========================
st.markdown('<div class="sec">Biodata</div>', unsafe_allow_html=True)
st.markdown(h('<div class="bd">' + "".join(f"<div><span>{k}</span><b>{v}</b></div>" for k, v in BIODATA) + "</div>"),
            unsafe_allow_html=True)

# =========================
# KEAHLIAN
# =========================
st.markdown('<div class="sec">Keahlian</div>', unsafe_allow_html=True)
st.markdown(h('<div class="chips">' + "".join(
    f'<div class="chip"><i style="background:{c};box-shadow:0 0 12px {c}"></i><b>{t}</b><span>{d}</span></div>'
    for t, d, c in SKILLS) + "</div>"), unsafe_allow_html=True)

# =========================
# PROYEK
# =========================
st.markdown('<div class="sec">Proyek</div>', unsafe_allow_html=True)
for col, (title, tech, color, desc) in zip(st.columns(2, gap="medium"), PROJECTS):
    with col:
        st.markdown(h(f'<div class="card" style="border-left:3px solid {color};"><h3>{title}</h3>'
                      f'<div class="tech" style="color:{color};">{tech}</div><p>{desc}</p></div>'), unsafe_allow_html=True)

# =========================
# KONTAK
# =========================
st.markdown('<div class="sec">Mari bekerja sama</div>', unsafe_allow_html=True)
for col, (label, text, url) in zip(st.columns(4, gap="medium"), CONTACTS):
    with col:
        st.markdown(h(f'<a class="contact" href="{url}" target="_blank"><small>{label}</small>{text}</a>'), unsafe_allow_html=True)
st.markdown('<a class="mail" href="mailto:aasyaddad@gmail.com">✉️ aasyaddad@gmail.com</a>', unsafe_allow_html=True)
st.markdown('<div class="foot">© 2026 Ahmad Asyaddad · Dibangun dengan Python (Streamlit)</div>', unsafe_allow_html=True)