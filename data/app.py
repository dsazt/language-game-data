import streamlit as st
import random

# Словарь переводов для "Рождественской песни"
TRANSLATIONS = {
    "Scrooge": "Скрудж", "Christmas": "Рождество", "Carol": "Песнь",
    "Marley": "Марли", "ghost": "призрак", "past": "прошлое",
    "present": "настоящее", "future": "будущее", "happy": "счастливый",
    "sad": "грустный", "cold": "холодный", "warm": "тёплый",
    "heart": "сердце", "soul": "душа", "money": "деньги",
    "work": "работа", "night": "ночь", "day": "день",
    "old": "старый", "good": "хороший", "bad": "плохой",
    "love": "любовь", "fear": "страх", "joy": "радость"
}

# Текст (первые строки "Рождественской песни")
TEXT = "Marley was dead Scrooge and Christmas Carol ghost past present future"

st.set_page_config(page_title="Рождественская песнь", page_icon="🎄")
st.title("🎄 Интерактивный переводчик")
st.subheader("Чарльз Диккенс «Рождественская песнь»")

# Инициализация
words = TEXT.split()
if 'states' not in st.session_state:
    st.session_state.states = [False] * len(words)

# Отображаем слова
st.markdown("### 👆 Кликайте на слова:")
cols = st.columns(4)

for i, word in enumerate(words):
    col = cols[i % 4]
    with col:
        clean = word.strip(".,!?")
        trans = TRANSLATIONS.get(clean, clean)
        display = trans if st.session_state.states[i] else word
        
        if st.button(display, key=f"b{i}", use_container_width=True):
            st.session_state.states[i] = not st.session_state.states[i]
            st.rerun()

# Статистика
done = sum(st.session_state.states)
st.progress(done / len(words))
st.caption(f"Переведено: {done} из {len(words)} слов")

# Кнопки управления
col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 Сбросить", use_container_width=True):
        st.session_state.states = [False] * len(words)
        st.rerun()
with col2:
    if st.button("✅ Перевести всё", use_container_width=True):
        st.session_state.states = [True] * len(words)
        st.rerun()

with st.expander("📌 Как это работает"):
    st.markdown("""
    - Приложение загружает словарь соответствий английских и русских слов
    - Пользователь кликает на слово → отображается перевод
    - Можно перевести все слова или сбросить
    - Подсчитывается прогресс обучения
    """)
