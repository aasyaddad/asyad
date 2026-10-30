import base64
from pathlib import Path

import streamlit as st

# =========================
# KONFIGURASI
# =========================
st.set_page_config(
    page_title="Ahmad Asyaddad | Developer Portfolio",
    page_icon="✳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).parent
PHOTO_PATH = BASE_DIR / "foto.jpg"

def image_to_base64(path):
    if path.exists():
        return base64.b64encode(path.read_bytes()).decode()
    return None

photo = image_to_base64(PHOTO_PATH)

# =========================
# DESAIN WEBSITE
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #080a0f;
    --panel: #10141d;
    --line: rgba(255,255,255,.11);
    --muted: #9299aa;
    --white: #f5f7fb;
    --cyan: #70f0db;
    --purple: #a58aff;
}

.stApp {
    background:
        radial-gradient(ellipse at 80% 0%, rgba(103,78,210,.14), transparent 32%),
        radial-gradient(ellipse at 5% 28%, rgba(54,218,199,.08), transparent 30%),
        var(--bg);
    color: var(--white);
    font-family: 'Manrope', sans-serif;
}

header, footer, #MainMenu {visibility: hidden;}
.block-container {
    max-width: 1200px;
    padding: 1.5rem 2rem 4rem;
}

html { scroll-behavior: smooth; }

p, li { color: #c0c5d1; line-height: 1.8; }

a { color: var(--cyan) !important; text-decoration: none !important; }

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 0 24px;
    border-bottom: 1px solid var(--line);
    margin-bottom: 55px;
}

.brand {
    color: var(--white);
    font-size: 17px;
    font-weight: 800;
    letter-spacing: -0.7px;
}

.brand span { color: var(--cyan); }

.nav-label {
    font: 11px 'DM Mono', monospace;
    color: var(--muted);
    letter-spacing: 1.4px;
}

.status {
    border: 1px solid rgba(112,240,219,.3);
    background: rgba(112,240,219,.07);
    border-radius: 30px;
    padding: 8px 13px;
    color: var(--cyan);
    font: 10px 'DM Mono', monospace;
    letter-spacing: .6px;
}

.eyebrow {
    color: var(--cyan);
    font: 11px 'DM Mono', monospace;
    letter-spacing: 2px;
    margin-bottom: 20px;
}

.hero-title {
    font-size: clamp(48px, 7vw, 88px);
    font-weight: 800;
    line-height: .99;
    letter-spacing: -5px;
    margin: 0 0 24px;
    color: var(--white);
}

.hero-title .gradient {
    background: linear-gradient(100deg, var(--cyan), #b7a4ff 75%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-desc {
    color: #a7afbf;
    font-size: 15px;
    max-width: 510px;
    line-height: 1.9;
    margin-bottom: 26px;
}

.mini-info {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    color: #a7afbf;
    font: 11px 'DM Mono', monospace;
    margin-top: 28px;
}

.mini-info span::before {
    content: "↗ ";
    color: var(--cyan);
}

.profile-frame {
    position: relative;
    background: linear-gradient(145deg, #202b39, #12131f 55%, #252044);
    border: 1px solid rgba(255,255,255,.14);
    border-radius: 28px;
    padding: 13px;
    box-shadow: 0 25px 100px rgba(0,0,0,.32);
}

.profile-inner {
    min-height: 360px;
    border-radius: 19px;
    overflow: hidden;
    position: relative;
    background:
        radial-gradient(circle at 50% 25%, rgba(112,240,219,.16), transparent 45%),
        #111722;
}

.profile-inner img {
    display: block;
    width: 100%;
    height: 390px;
    object-fit: cover;
    object-position: center 35%;
}

.photo-placeholder {
    height: 360px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    color: var(--cyan);
    font-size: 65px;
}

.photo-caption {
    position: absolute;
    bottom: 15px;
    left: 15px;
    right: 15px;
    padding: 14px;
    background: rgba(8,10,15,.82);
    border: 1px solid var(--line);
    border-radius: 13px;
    backdrop-filter: blur(12px);
}

.photo-caption strong {
    display: block;
    color: white;
    font-size: 13px;
}

.photo-caption small {
    color: var(--cyan);
    font: 10px 'DM Mono', monospace;
}

.section-head {
    display: flex;
    justify-content: space-between;
    align-items: end;
    border-bottom: 1px solid var(--line);
    padding-bottom: 18px;
    margin: 78px 0 28px;
}

.section-kicker {
    color: var(--cyan);
    font: 11px 'DM Mono', monospace;
    letter-spacing: 2px;
}

.section-title {
    color: var(--white);
    font-size: clamp(28px, 4vw, 43px);
    font-weight: 800;
    letter-spacing: -2px;
    margin: 8px 0 0;
}

.section-count {
    color: #727b8e;
    font: 12px 'DM Mono', monospace;
}

.about-panel, .skill-card, .project-card, .contact-panel {
    background: linear-gradient(145deg, rgba(255,255,255,.045), rgba(255,255,255,.012));
    border: 1px solid var(--line);
    border-radius: 20px;
    padding: 25px;
    height: 100%;
    transition: border-color .2s, transform .2s;
}

.skill-card:hover, .project-card:hover {
    border-color: rgba(112,240,219,.55);
    transform: translateY(-4px);
}

.card-index {
    color: var(--cyan);
    font: 11px 'DM Mono', monospace;
    margin-bottom: 28px;
}

.card-title {
    font-size: 20px;
    font-weight: 800;
    letter-spacing: -.5px;
    color: white;
    margin-bottom: 10px;
}

.card-copy {
    color: #9da5b5;
    font-size: 13px;
    line-height: 1.8;
}

.skill-name {
    color: white;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 10px;
}

.tag {
    display: inline-block;
    border: 1px solid var(--line);
    color: #c2c9d7;
    border-radius: 6px;
    padding: 5px 9px;
    margin: 5px 5px 0 0;
    font: 10px 'DM Mono', monospace;
}

.project-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 28px;
}

.project-number {
    color: var(--cyan);
    font: 12px 'DM Mono', monospace;
}

.project-icon {
    width: 44px;
    height: 44px;
    border: 1px solid var(--line);
    border-radius: 13px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
}

.project-title {
    color: white;
    font-size: 23px;
    font-weight: 800;
    letter-spacing: -.7px;
    margin-bottom: 12px;
}

.project-footer {
    border-top: 1px solid var(--line);
    padding-top: 17px;
    margin-top: 22px;
    color: var(--cyan);
    font: 10px 'DM Mono', monospace;
}

.contact-panel {
    background:
      radial-gradient(ellipse at 100% 0%, rgba(165,138,255,.12), transparent 40%),
      linear-gradient(120deg, rgba(112,240,219,.07), rgba(255,255,255,.015));
    padding: 35px;
}

.contact-title {
    color: white;
    font-size: clamp(32px, 5vw, 52px);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -2.5px;
    margin: 12px 0 18px;
}

.footer {
    border-top: 1px solid var(--line);
    margin-top: 70px;
    padding-top: 22px;
    display: flex;
    justify-content: space-between;
    gap: 15px;
    flex-wrap: wrap;
    color: #737c8e;
    font: 10px 'DM Mono', monospace;
}

div.stButton > button, div.stLinkButton > a {
    border-radius: 10px !important;
    min-height: 43px;
    font-weight: 700 !important;
}

div.stButton > button[kind="primary"] {
    background: var(--cyan) !important;
    color: #07110f !important;
    border: 1px solid var(--cyan) !important;
}

div.stLinkButton > a {
    border: 1px solid rgba(255,255,255,.2) !important;
    color: white !important;
    background: rgba(255,255,255,.03) !important;
}

@media (max-width: 700px) {
    .block-container {padding: 1rem 1.1rem 3rem;}
    .hero-title {letter-spacing: -3px;}
    .topbar {margin-bottom: 35px;}
    .section-head {margin-top: 50px;}
}
</style>
""", unsafe_allow_html=True)

# =========================
# NAVIGASI
# =========================
st.markdown("""
<div class="topbar">
  <div class="brand">AA<span>✳</span> / PORTFOLIO</div>
  <div class="nav-label">INFORMATICS · UNESA</div>
  <div class="status">● OPEN TO LEARN</div>
</div>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
left, right = st.columns([1.25, 0.85], gap="large", vertical_alignment="center")

with left:
    st.markdown("""
    <div class="eyebrow">HELLO, WORLD — I'M</div>
    <div class="hero-title">
      Ahmad<br>
      <span class="gradient">Asyaddad.</span>
    </div>
    <div class="hero-desc">
      Mahasiswa Teknik Informatika yang tertarik pada dunia teknologi,
      pengembangan aplikasi, dan eksplorasi ide menjadi solusi digital
      yang bermanfaat.
    </div>
    <div class="mini-info">
      <span>BASED IN SURABAYA</span>
      <span>INFORMATICS STUDENT</span>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    a, b = st.columns([1, 1])
    with a:
        st.button(
            "Kenali Saya ↓",
            type="primary",
            use_container_width=True,
            on_click=lambda: st.session_state.update({"jump_about": True}),
        )
    with b:
        st.link_button(
            "Hubungi Saya ↗",
            "mailto:aasyaddad@gmail.com",
            use_container_width=True,
        )

with right:
    if photo:
        photo_html = f"""
        <div class="profile-frame">
          <div class="profile-inner">
            <img src="data:image/jpeg;base64,{photo}" alt="Foto Ahmad Asyaddad">
            <div class="photo-caption">
              <strong>Ahmad Asyaddad</strong>
              <small>STUDENT · DEVELOPER IN PROGRESS</small>
            </div>
          </div>
        </div>
        """
    else:
        photo_html = """
        <div class="profile-frame">
          <div class="profile-inner">
            <div class="photo-placeholder">✳
              <div style="font-size:12px;color:#a7afbf;margin-top:12px">
                Tambahkan foto.jpg
              </div>
            </div>
          </div>
        </div>
        """
    st.markdown(photo_html, unsafe_allow_html=True)

# =========================
# ABOUT
# =========================
st.markdown("""
<div id="about" class="section-head">
  <div>
    <div class="section-kicker">01 / INTRODUCTION</div>
    <div class="section-title">Sedikit tentang saya.</div>
  </div>
  <div class="section-count">WHO I AM</div>
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns([1.15, 0.85], gap="large")

with c1:
    st.markdown("""
    <div class="about-panel">
      <div class="card-index">PROFILE — 001</div>
      <div class="card-title">Belajar. Membangun. Berkembang.</div>
      <div class="card-copy">
        Saya percaya bahwa kemampuan berkembang melalui rasa ingin tahu,
        konsistensi, dan keberanian mencoba hal baru. Saat ini saya terus
        mempelajari pemrograman serta membangun proyek untuk meningkatkan
        kemampuan teknis dan pengalaman praktis.
        <br><br>
        Di luar teknologi, saya menikmati badminton, musik, dan menjelajahi
        tempat baru untuk mendapatkan pengalaman serta inspirasi.
      </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="about-panel">
      <div class="card-index">QUICK FACTS — 002</div>
      <div class="card-title">The essentials.</div>
      <div class="card-copy">
        <b style="color:white">Nama</b><br>Ahmad Asyaddad<br><br>
        <b style="color:white">Fokus</b><br>Informatika & pengembangan aplikasi<br><br>
        <b style="color:white">Lokasi</b><br>Surabaya, Indonesia<br><br>
        <b style="color:white">Di luar layar</b><br>Badminton · Musik · Eksplorasi
      </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# SKILLS
# =========================
st.markdown("""
<div class="section-head">
  <div>
    <div class="section-kicker">02 / TOOLKIT</div>
    <div class="section-title">Tools I work with.</div>
  </div>
  <div class="section-count">CURRENT SKILLS</div>
</div>
""", unsafe_allow_html=True)

s1, s2, s3 = st.columns(3, gap="medium")

skills = [
    ("01", "Python", "Mempelajari logika program dan membangun aplikasi.", ["PYTHON", "LOGIC"]),
    ("02", "Web Development", "Mengenal struktur dan pengembangan pengalaman web.", ["HTML", "CSS", "STREAMLIT"]),
    ("03", "Problem Solving", "Melatih cara berpikir sistematis dalam menyelesaikan masalah.", ["ANALYTICAL", "LEARNING"]),
]

for col, (num, name, desc, tags) in zip([s1, s2, s3], skills):
    with col:
        tag_html = "".join(f'<span class="tag">{tag}</span>' for tag in tags)
        st.markdown(f"""
        <div class="skill-card">
          <div class="card-index">{num} / SKILLSET</div>
          <div class="skill-name">{name}</div>
          <div class="card-copy">{desc}</div>
          <div style="margin-top:18px">{tag_html}</div>
        </div>
        """, unsafe_allow_html=True)

# =========================
# PROJECTS
# =========================
st.markdown("""
<div class="section-head">
  <div>
    <div class="section-kicker">03 / SELECTED WORK</div>
    <div class="section-title">Things I'm building.</div>
  </div>
  <div class="section-count">PROJECT ARCHIVE</div>
</div>
""", unsafe_allow_html=True)

p1, p2 = st.columns(2, gap="medium")

with p1:
    st.markdown("""
    <div class="project-card">
      <div class="project-top">
        <div class="project-number">PROJECT / 001</div>
        <div class="project-icon">⌘</div>
      </div>
      <div class="project-title">B-INFESA Web App</div>
      <div class="card-copy">
        Konsep aplikasi web untuk mendukung kebutuhan informasi dan
        aktivitas kelas dengan pendekatan yang terstruktur dan mudah digunakan.
      </div>
      <div style="margin-top:15px">
        <span class="tag">PYTHON</span>
        <span class="tag">FLASK</span>
        <span class="tag">WEB APP</span>
      </div>
      <div class="project-footer">WEB DEVELOPMENT &nbsp; ↗</div>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="project-card">
      <div class="project-top">
        <div class="project-number">PROJECT / 002</div>
        <div class="project-icon">▦</div>
      </div>
      <div class="project-title">Sistem Absensi INF26B</div>
      <div class="card-copy">
        Konsep aplikasi pencatatan kehadiran mahasiswa untuk membantu
        proses pengelolaan data absensi kelas secara lebih praktis.
      </div>
      <div style="margin-top:15px">
        <span class="tag">PYTHON</span>
        <span class="tag">STREAMLIT</span>
        <span class="tag">DATA</span>
      </div>
      <div class="project-footer">APPLICATION DEVELOPMENT &nbsp; ↗</div>
    </div>
    """, unsafe_allow_html=True)

st.caption(
    "Catatan: sesuaikan deskripsi dan teknologi proyek dengan fitur yang "
    "benar-benar sudah kamu buat."
)

# =========================
# CONTACT
# =========================
st.markdown("""
<div class="section-head">
  <div>
    <div class="section-kicker">04 / LET'S CONNECT</div>
    <div class="section-title">Punya ide menarik?</div>
  </div>
  <div class="section-count">CONTACT</div>
</div>
<div class="contact-panel">
  <div class="section-kicker">OPEN FOR CONNECTIONS</div>
  <div class="contact-title">
    Let's make something<br>meaningful.
  </div>
  <div class="card-copy">
    Saya terbuka untuk belajar, bertukar ide, dan terhubung dengan orang
    yang tertarik pada teknologi serta pengembangan diri.
  </div>
</div>
""", unsafe_allow_html=True)

st.write("")
contact1, contact2, contact3 = st.columns(3)

with contact1:
    st.link_button(
        "Email ↗",
        "mailto:aasyaddad@gmail.com",
        use_container_width=True,
    )

with contact2:
    st.link_button(
        "Instagram ↗",
        "https://instagram.com/ahmad_asyaddad",
        use_container_width=True,
    )

with contact3:
    st.link_button(
        "WhatsApp ↗",
        "https://wa.me/6281330419416",
        use_container_width=True,
    )

st.markdown("""
<div class="footer">
  <span>© 2026 AHMAD ASYADDAD</span>
  <span>DESIGNED WITH CURIOSITY · BUILT WITH STREAMLIT</span>
</div>
""", unsafe_allow_html=True)