import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📚 2차 곡선 탐험기")
st.write("2차 곡선의 매개변수를 바꾸며 그래프의 변화를 관찰해 보세요.")

# --- 사이드바: 도형 선택 및 매개변수 입력 ---
with st.sidebar:
    st.header("설정")
    conic_type = st.selectbox(
        "2차 곡선 종류를 선택하세요:",
        ("포물선", "타원", "쌍곡선")
    )

    if conic_type == "포물선":
        st.latex(r"y^2 = 4px")
        p = st.number_input("p 값을 입력하세요:", value=1.0, step=0.1)
    
    elif conic_type == "타원":
        st.latex(r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1")
        a = st.number_input("a 값을 입력하세요 (장축):", min_value=0.1, value=5.0, step=0.1)
        b = st.number_input("b 값을 입력하세요 (단축):", min_value=0.1, value=3.0, step=0.1)
    
    elif conic_type == "쌍곡선":
        st.latex(r"\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1")
        a = st.number_input("a 값을 입력하세요:", min_value=0.1, value=3.0, step=0.1)
        b = st.number_input("b 값을 입력하세요:", min_value=0.1, value=4.0, step=0.1)


# --- 메인 영역: 그래프 및 결과 표시 ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')
ax.grid()
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# 2차 곡선 유형별 계산 및 플롯
if conic_type == "포물선":
    if p != 0:
        x_vals = np.linspace(-10, 10, 400)
        y_vals_pos = np.sqrt(4 * p * x_vals)
        y_vals_neg = -np.sqrt(4 * p * x_vals)
        ax.plot(x_vals, y_vals_pos, color='blue', label='$y^2 = 4px$')
        ax.plot(x_vals, y_vals_neg, color='blue')

        # 초점과 준선 표시
        ax.plot(p, 0, 'ro', label='초점 F')
        ax.axvline(-p, color='red', linestyle='--', label='준선')
        
        st.write(f"**초점 (F)**: $({p}, 0)$")
        st.write(f"**준선**: $x = -{p}$")

elif conic_type == "타원":
    if a > b:
        c = np.sqrt(a**2 - b**2)
        theta = np.linspace(0, 2 * np.pi, 400)
        x_vals = a * np.cos(theta)
        y_vals = b * np.sin(theta)
        ax.plot(x_vals, y_vals, color='green', label=r'$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$')

        # 초점 표시
        ax.plot(c, 0, 'go', label='초점 F')
        ax.plot(-c, 0, 'go')
        
        st.write(f"**초점**: $(\pm{c:.2f}, 0)$")
        st.write(f"**장축의 길이**: $2a = {2*a}$")
        st.write(f"**단축의 길이**: $2b = {2*b}$")
    else:
        st.warning("타원의 경우, a는 b보다 커야 합니다.")

elif conic_type == "쌍곡선":
    if a != 0 and b != 0:
        c = np.sqrt(a**2 + b**2)
        x_vals = np.linspace(-10, 10, 400)
        
        y_vals_pos = np.sqrt((x_vals**2 / a**2 - 1)) * b
        y_vals_neg = -np.sqrt((x_vals**2 / a**2 - 1)) * b
        
        ax.plot(x_vals, y_vals_pos, color='purple', label=r'$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$')
        ax.plot(x_vals, y_vals_neg, color='purple')

        # 점근선과 초점 표시
        asymptote_y1 = (b/a) * x_vals
        asymptote_y2 = -(b/a) * x_vals
        ax.plot(x_vals, asymptote_y1, 'k--', label='점근선')
        ax.plot(x_vals, asymptote_y2, 'k--')
        
        ax.plot(c, 0, 'mo', label='초점 F')
        ax.plot(-c, 0, 'mo')
        
        st.write(f"**초점**: $(\pm{c:.2f}, 0)$")
        st.write(f"**점근선**: $y = \pm{b/a:.2f}x$")

ax.legend()
plt.title(f"{conic_type} 그래프")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-10, 10)
plt.ylim(-10, 10)

st.pyplot(fig)
