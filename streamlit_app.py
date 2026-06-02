import streamlit as st

# =====================================
# CONFIG
# =====================================
st.set_page_config(
    page_title="ThermoCalcz",
    page_icon="🌌",
    layout="wide"
)

# =====================================
# CSS FUTURISTIK SUPER UPGRADE
# =====================================
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(-45deg, #020617, #1e1b4b, #0f172a, #581c87, #3b0764);
    background-size: 500% 500%;
    animation: gradientBG 18s ease infinite;
    color:white;
}

@keyframes gradientBG {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

.title {
    text-align:center;
    font-size:68px;
    font-weight:900;
    background: linear-gradient(to right,#93c5fd,#dbeafe,#60a5fa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    text-shadow:0 0 30px rgba(59,130,246,.8);
    animation: floatTitle 3s ease-in-out infinite;
}

@keyframes floatTitle {
    0% {transform:translateY(0px);}
    50% {transform:translateY(-8px);}
    100% {transform:translateY(0px);}
}

.subtitle {
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:35px;
}

.result {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(18px);
    color:white;
    padding:25px;
    border-radius:22px;
    border:1px solid rgba(255,255,255,0.15);
    box-shadow:0 8px 40px rgba(0,0,0,.35);
    animation: fadeIn 0.7s ease;
    margin-top:20px;
}

@keyframes fadeIn {
    from { opacity:0; transform:translateY(20px); }
    to { opacity:1; transform:translateY(0); }
}

.stButton>button {
    width:100%;
    padding:15px;
    border-radius:18px;
    font-weight:700;
    font-size:16px;
    border:none;
    color:white;
    background: linear-gradient(135deg, #7c3aed, #d946ef);
    box-shadow:0 0 18px rgba(217, 70, 239, 0.5);
    transition:all .3s ease;
}

.stButton>button:hover {
    transform:translateY(-6px) scale(1.02);
    box-shadow:0 0 30px rgba(217, 70, 239, 0.9);
}

.stNumberInput input, .stTextInput input, .stTextArea textarea {
    background-color: rgba(255, 255, 255, 0.9) !important;
    color: #000000 !important;
    border-radius:15px !important;
    font-weight: 600 !important;
}

[data-testid="stWidgetLabel"] p {
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    text-shadow: 0 0 8px rgba(255,255,255,0.4);
}

.katex {
    color:#f5d0fe !important;
    font-size:24px !important;
}

.stAlert {
    border-radius:18px;
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(216,180,254,0.25) !important;
    backdrop-filter: blur(10px);
}

.stAlert p { color: #f5d0fe !important; font-weight: 500; }
.stAlert svg { fill: #d8b4fe !important; }
h1,h2,h3 { color:#f5d0fe; }
</style>
""", unsafe_allow_html=True)

# =====================================
# UTILITIES
# =====================================
def fmt(angka):
    try:
        return f"{angka:g}"
    except:
        return str(angka)

# =====================================
# SESSION
# =====================================
if "menu" not in st.session_state:
    st.session_state.menu = None

menu_list = [
    "Hukum 1 Termodinamika", "Usaha", "Kalor", "Entalpi", "Hukum Hess",
    "ΔH Reaksi", "Energi Gibbs", "Entropi", "Gas Ideal", "Gas Nyata",
    "Asisten Soal Cerita"
]

# =====================================
# HOME
# =====================================
if st.session_state.menu is None:
    st.snow()
    st.markdown("<div class='title'>🌌 ThermoVerse ⚗️</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Kalkulator Termodinamika Universal — Cari Variabel Apa Saja</div>", unsafe_allow_html=True)

    cols = st.columns(2)
    for i, m in enumerate(menu_list):
        with cols[i % 2]:
            if st.button(f"⚡ {m}"):
                st.session_state.menu = m
                st.rerun()

# =====================================
# CALCULATOR PAGE
# =====================================
else:
    menu = st.session_state.menu

    if st.button("⬅️ Kembali"):
        st.session_state.menu = None
        st.rerun()

    st.header(f"⚗️ {menu}")
    st.divider()

    # -------------------------------------
    # 1. HUKUM 1 TERMODINAMIKA (ΔU = Q - W)
    # -------------------------------------
    if menu == "Hukum 1 Termodinamika":
        st.latex(r"\Delta U = Q - W")
        target = st.selectbox("Pilih variabel yang ingin dicari:", ["ΔU (Perubahan Energi Dalam)", "Q (Kalor)", "W (Usaha)"])
        
        Q = st.number_input("Q (kJ)", value=0.0) if target != "Q (Kalor)" else 0.0
        W = st.number_input("W (kJ)", value=0.0) if target != "W (Usaha)" else 0.0
        dU = st.number_input("ΔU (kJ)", value=0.0) if target != "ΔU (Perubahan Energi Dalam)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "ΔU" in target:
                hasil = Q - W
                langkah = f"ΔU = Q - W <br> ΔU = {fmt(Q)} - {fmt(W)} <br> ΔU = <b>{fmt(hasil)} kJ</b>"
            elif "Q" in target:
                hasil = dU + W
                langkah = f"Q = ΔU + W <br> Q = {fmt(dU)} + {fmt(W)} <br> Q = <b>{fmt(hasil)} kJ</b>"
            else:
                hasil = Q - dU
                langkah = f"W = Q - ΔU <br> W = {fmt(Q)} - {fmt(dU)} <br> W = <b>{fmt(hasil)} kJ</b>"
            
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # -------------------------------------
    # 2. USAHA (W = P * dV)
    # -------------------------------------
    elif menu == "Usaha":
        st.latex(r"W = P \cdot \Delta V")
        target = st.selectbox("Pilih variabel yang ingin dicari:", ["W (Usaha)", "P (Tekanan)", "ΔV (Perubahan Volume)"])

        W = st.number_input("W (J)", value=0.0) if target != "W (Usaha)" else 0.0
        P = st.number_input("P (Pa)", value=0.0) if target != "P (Tekanan)" else 0.0
        dV = st.number_input("ΔV (m³)", value=0.0) if target != "ΔV (Perubahan Volume)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "W" in target:
                hasil = P * dV
                langkah = f"W = P × ΔV <br> W = {fmt(P)} × {fmt(dV)} <br> W = <b>{fmt(hasil)} J</b>"
            elif "P" in target:
                hasil = W / dV if dV != 0 else 0
                langkah = f"P = W / ΔV <br> P = {fmt(W)} / {fmt(dV)} <br> P = <b>{fmt(hasil)} Pa</b>"
            else:
                hasil = W / P if P != 0 else 0
                langkah = f"ΔV = W / P <br> ΔV = {fmt(W)} / {fmt(P)} <br> ΔV = <b>{fmt(hasil)} m³</b>"
            
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # -------------------------------------
    # 3. KALOR (Q = m * c * dT)
    # -------------------------------------
    elif menu == "Kalor":
        st.latex(r"Q = m \cdot c \cdot \Delta T")
        target = st.selectbox("Pilih variabel yang ingin dicari:", ["Q (Kalor)", "m (Massa)", "c (Kalor Jenis)", "ΔT (Perubahan Suhu)"])

        Q = st.number_input("Q (J)", value=0.0) if target != "Q (Kalor)" else 0.0
        m = st.number_input("m (g)", value=0.0) if target != "m (Massa)" else 0.0
        c = st.number_input("c (J/g°C)", value=0.0) if target != "c (Kalor Jenis)" else 0.0
        dT = st.number_input("ΔT (K atau °C)", value=0.0) if target != "ΔT (Perubahan Suhu)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "Q" in target:
                hasil = m * c * dT
                langkah = f"Q = m × c × ΔT <br> Q = {fmt(m)} × {fmt(c)} × {fmt(dT)} <br> Q = <b>{fmt(hasil)} J</b>"
            elif "m" in target:
                hasil = Q / (c * dT) if (c * dT) != 0 else 0
                langkah = f"m = Q / (c × ΔT) <br> m = {fmt(Q)} / ({fmt(c)} × {fmt(dT)}) <br> m = <b>{fmt(hasil)} g</b>"
            elif "c" in target:
                hasil = Q / (m * dT) if (m * dT) != 0 else 0
                langkah = f"c = Q / (m × ΔT) <br> c = {fmt(Q)} / ({fmt(m)} × {fmt(dT)}) <br> c = <b>{fmt(hasil)} J/g°C</b>"
            else:
                hasil = Q / (m * c) if (m * c) != 0 else 0
                langkah = f"ΔT = Q / (m × c) <br> ΔT = {fmt(Q)} / ({fmt(m)} × {fmt(c)}) <br> ΔT = <b>{fmt(hasil)} K</b>"
            
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # -------------------------------------
    # 4. ENTALPI (ΔH = ΔU + ΔnRT)
    # -------------------------------------
    elif menu == "Entalpi":
        st.latex(r"\Delta H = \Delta U + \Delta n \cdot R \cdot T")
        target = st.selectbox("Pilih variabel yang ingin dicari:", ["ΔH (Entalpi)", "ΔU (Energi Dalam)", "Δn (Perubahan Mol)", "T (Suhu)"])
        R = 0.008314  # kJ/mol.K

        dH = st.number_input("ΔH (kJ)", value=0.0) if target != "ΔH (Entalpi)" else 0.0
        dU = st.number_input("ΔU (kJ)", value=0.0) if target != "ΔU (Energi Dalam)" else 0.0
        dn = st.number_input("Δn (mol)", value=0.0) if target != "Δn (Perubahan Mol)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "ΔH" in target:
                hasil = dU + (dn * R * T)
                langkah = f"ΔH = ΔU + (Δn × R × T) <br> ΔH = {fmt(dU)} + ({fmt(dn)} × {R} × {fmt(T)}) <br> ΔH = <b>{fmt(hasil)} kJ</b>"
            elif "ΔU" in target:
                hasil = dH - (dn * R * T)
                langkah = f"ΔU = ΔH - (Δn × R × T) <br> ΔU = {fmt(dH)} - ({fmt(dn)} × {R} × {fmt(T)}) <br> ΔU = <b>{fmt(hasil)} kJ</b>"
            elif "Δn" in target:
                hasil = (dH - dU) / (R * T) if T != 0 else 0
                langkah = f"Δn = (ΔH - ΔU) / (R × T) <br> Δn = ({fmt(dH)} - {fmt(dU)}) / ({R} × {fmt(T)}) <br> Δn = <b>{fmt(hasil)} mol</b>"
            else:
                hasil = (dH - dU) / (dn * R) if dn != 0 else 0
                langkah = f"T = (ΔH - ΔU) / (Δn × R) <br> T = ({fmt(dH)} - {fmt(dU)}) / ({fmt(dn)} × {R}) <br> T = <b>{fmt(hasil)} K</b>"
            
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # -------------------------------------
    # 5. HUKUM HESS (Mencari salah satu ΔH dari total)
    # -------------------------------------
    elif menu == "Hukum Hess":
        st.latex(r"\Delta H_{total} = \Delta H_1 + \Delta H_2 + ... + \Delta H_n")
        target = st.selectbox("Pilih operasi:", ["Hitung ΔH Total dari list", "Cari satu ΔH yang hilang"])

        if target == "Hitung ΔH Total dari list":
            data = st.text_input("Masukkan semua nilai ΔH (pisahkan dengan koma)", "10,-20,30")
            if st.button("Hitung"):
                arr = [float(x) for x in data.split(",") if x.strip() != ""]
                st.balloons()
                st.markdown(f"<div class='result'><h3>Hasil</h3>ΣΔH = <b>{fmt(sum(arr))} kJ</b></div>", unsafe_allow_html=True)
        else:
            total_h = st.number_input("Masukkan ΔH Total", value=0.0)
            data_parsial = st.text_input("Masukkan ΔH komponen lain yang diketahui (pisahkan dengan koma)", "10,-20")
            if st.button("Hitung"):
                arr = [float(x) for x in data_parsial.split(",") if x.strip() != ""]
                hasil = total_h - sum(arr)
                st.balloons()
                st.markdown(f"<div class='result'><h3>Hasil Variabel Hilang</h3>ΔH_x = ΔH_total - ΣΔH_diketahui <br> ΔH_x = {fmt(total_h)} - {fmt(sum(arr))} <br> ΔH_x = <b>{fmt(hasil)} kJ</b></div>", unsafe_allow_html=True)

    # -------------------------------------
    # 6. ΔH REAKSI (ΔH = ΣHf_produk - ΣHf_reaktan)
    # -------------------------------------
    elif menu == "ΔH Reaksi":
        st.latex(r"\Delta H = \sum Hf_{produk} - \sum Hf_{reaktan}")
        target = st.selectbox("Pilih variabel yang ingin dicari:", ["ΔH Reaksi", "ΣHf Produk", "ΣHf Reaktan"])

        dH = st.number_input("ΔH Reaksi (kJ)", value=0.0) if target != "ΔH Reaksi" else 0.0
        prod = st.text_input("Masukkan nilai Produk (jika lebih dari satu, pisah koma)", "0") if target != "ΣHf Produk" else "0"
        reak = st.text_input("Masukkan nilai Reaktan (jika lebih dari satu, pisah koma)", "0") if target != "ΣHf Reaktan" else "0"

        if st.button("Hitung"):
            st.balloons()
            p_sum = sum([float(x) for x in prod.split(",") if x.strip() != ""])
            r_sum = sum([float(x) for x in reak.split(",") if x.strip() != ""])

            if target == "ΔH Reaksi":
                hasil = p_sum - r_sum
                langkah = f"ΔH = ΣHf_produk - ΣHf_reaktan <br> ΔH = {fmt(p_sum)} - {fmt(r_sum)} <br> ΔH = <b>{fmt(hasil)} kJ/mol</b>"
            elif target == "ΣHf Produk":
                hasil = dH + r_sum
                langkah = f"ΣHf_produk = ΔH + ΣHf_reaktan <br> ΣHf_produk = {fmt(dH)} + {fmt(r_sum)} <br> ΣHf_produk = <b>{fmt(hasil)} kJ/mol</b>"
            else:
                hasil = p_sum - dH
                langkah = f"ΣHf_reaktan = ΣHf_produk - ΔH <br> ΣHf_reaktan = {fmt(p_sum)} - {fmt(dH)} <br> ΣHf_reaktan = <b>{fmt(hasil)} kJ/mol</b>"
            
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # -------------------------------------
    # 7. ENERGI GIBBS (ΔG = ΔH - T * dS)
    # -------------------------------------
    elif menu == "Energi Gibbs":
        st.latex(r"\Delta G = \Delta H - T \cdot \Delta S")
        target = st.selectbox("Pilih variabel yang ingin dicari:", ["ΔG (Energi Gibbs)", "ΔH (Entalpi)", "T (Suhu dalam K)", "ΔS (Entropi dalam kJ/K)"])

        dG = st.number_input("ΔG (kJ)", value=0.0) if target != "ΔG (Energi Gibbs)" else 0.0
        dH = st.number_input("ΔH (kJ)", value=0.0) if target != "ΔH (Entalpi)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu dalam K)" else 0.0
        dS = st.number_input("ΔS (kJ/K)", value=0.0) if target != "ΔS (Entropi dalam kJ/K)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "ΔG" in target:
                hasil = dH - (T * dS)
                langkah = f"ΔG = ΔH - (T × ΔS) <br> ΔG = {fmt(dH)} - ({fmt(T)} × {fmt(dS)}) <br> ΔG = <b>{fmt(hasil)} kJ</b>"
            elif "ΔH" in target:
                hasil = dG + (T * dS)
                langkah = f"ΔH = ΔG + (T × ΔS) <br> ΔH = {fmt(dG)} + ({fmt(T)} × {fmt(dS)}) <br> ΔH = <b>{fmt(hasil)} kJ</b>"
            elif "T" in target:
                hasil = (dH - dG) / dS if dS != 0 else 0
                langkah = f"T = (ΔH - ΔG) / ΔS <br> T = ({fmt(dH)} - {fmt(dG)}) / {fmt(dS)} <br> T = <b>{fmt(hasil)} K</b>"
            else:
                hasil = (dH - dG) / T if T != 0 else 0
                langkah = f"ΔS = (ΔH - ΔG) / T <br> ΔS = ({fmt(dH)} - {fmt(dG)}) / {fmt(T)} <br> ΔS = <b>{fmt(hasil)} kJ/K</b>"
            
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # -------------------------------------
    # 8. ENTROPI (ΔS = Q / T)
    # -------------------------------------
    elif menu == "Entropi":
        st.latex(r"\Delta S = \frac{Q}{T}")
        target = st.selectbox("Pilih variabel yang ingin dicari:", ["ΔS (Entropi)", "Q (Kalor)", "T (Suhu)"])

        dS = st.number_input("ΔS (kJ/K)", value=0.0) if target != "ΔS (Entropi)" else 0.0
        Q = st.number_input("Q (kJ)", value=0.0) if target != "Q (Kalor)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "ΔS" in target:
                hasil = Q / T if T != 0 else 0
                langkah = f"ΔS = Q / T <br> ΔS = {fmt(Q)} / {fmt(T)} <br> ΔS = <b>{fmt(hasil)} kJ/K</b>"
            elif "Q" in target:
                hasil = dS * T
                langkah = f"Q = ΔS × T <br> Q = {fmt(dS)} × {fmt(T)} <br> Q = <b>{fmt(hasil)} kJ</b>"
            else:
                hasil = Q / dS if dS != 0 else 0
                langkah = f"T = Q / ΔS <br> T = {fmt(Q)} / {fmt(dS)} <br> T = <b>{fmt(hasil)} K</b>"
            
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # -------------------------------------
    # 9. GAS IDEAL (PV = nRT)
    # -------------------------------------
    elif menu == "Gas Ideal":
        st.latex(r"P \cdot V = n \cdot R \cdot T")
        target = st.selectbox("Pilih variabel yang ingin dicari:", ["P (Tekanan)", "V (Volume)", "n (Jumlah Mol)", "T (Suhu)"])
        R = 0.0821

        P = st.number_input("P (atm)", value=0.0) if target != "P (Tekanan)" else 0.0
        V = st.number_input("V (L)", value=0.0) if target != "V (Volume)" else 0.0
        n = st.number_input("n (mol)", value=0.0) if target != "n (Jumlah Mol)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "P" in target:
                hasil = (n * R * T) / V if V != 0 else 0
                langkah = f"P = (nRT) / V <br> P = ({fmt(n)} × {R} × {fmt(T)}) / {fmt(V)} <br> P = <b>{fmt(hasil)} atm</b>"
            elif "V" in target:
                hasil = (n * R * T) / P if P != 0 else 0
                langkah = f"V = (nRT) / P <br> V = ({fmt(n)} × {R} × {fmt(T)}) / {fmt(P)} <br> V = <b>{fmt(hasil)} L</b>"
            elif "n" in target:
                hasil = (P * V) / (R * T) if T != 0 else 0
                langkah = f"n = (PV) / (RT) <br> n = ({fmt(P)} × {fmt(V)}) / ({R} × {fmt(T)}) <br> n = <b>{fmt(hasil)} mol</b>"
            else:
                hasil = (P * V) / (n * R) if n != 0 else 0
                langkah = f"T = (PV) / (nR) <br> T = ({fmt(P)} × {fmt(V)}) / ({fmt(n)} × {R}) <br> T = <b>{fmt(hasil)} K</b>"
            
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # -------------------------------------
    # 10. GAS NYATA (Van der Waals)
    # -------------------------------------
    elif menu == "Gas Nyata":
        st.latex(r"\left(P + \frac{an^2}{V^2}\right)(V - nb) = nRT")
        target = st.selectbox("Pilih variabel yang ingin dicari:", ["P (Tekanan)", "T (Suhu)"])
        R = 0.0821

        n = st.number_input("n (mol)", value=0.0)
        V = st.number_input("V (L)", value=0.0)
        a = st.number_input("a (atm.L²/mol²)", value=0.0)
        b = st.number_input("b (L/mol)", value=0.0)
        
        P = st.number_input("P (atm)", value=0.0) if target != "P (Tekanan)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "P" in target:
                if (V - n * b) != 0 and V != 0:
                    hasil = ((n * R * T) / (V - n * b)) - ((a * (n ** 2)) / (V ** 2))
                else:
                    hasil = 0
                langkah = f"P = [nRT / (V - nb)] - [an² / V²] <br> P = <b>{fmt(hasil)} atm</b>"
            else:
                if n != 0 and (V - n * b) != 0:
                    hasil = ((P + (a * (n**2) / (V**2))) * (V - n * b)) / (n * R)
                else:
                    hasil = 0
                langkah = f"T = [(P + an²/V²)(V - nb)] / nR <br> T = <b>{fmt(hasil)} K</b>"
            
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # -------------------------------------
    # 11. ASISTEN SOAL CERITA (Smart Parser)
    # -------------------------------------
    elif menu == "Asisten Soal Cerita":
        st.subheader("🤖 Smart Solver Soal Cerita")
        st.write("Masukkan teks soal cerita termodinamika Anda di bawah ini. Sis
