import streamlit as st
import openai

# Ensure you have in your requirements.txt:
# streamlit
# openai>=1.0.0

st.title("Простейшее приложение для OpenAI")
st.write("Введите ваш OpenAI API ключ и запрос, чтобы получить ответ от модели GPT-3.5-turbo.")

# Поле для ввода API-ключа
api_key = st.text_input("OpenAI API Key:", type="password")
if not api_key:
    st.warning("Пожалуйста, введите ваш OpenAI API ключ для продолжения.")
    st.stop()

openai.api_key = api_key

# Поле для ввода запроса
prompt = st.text_area("Ваш запрос:")

if st.button("Отправить запрос"):
    if prompt:
        with st.spinner("Обработка запроса..."):
            try:
                # Используем новый интерфейс openai.chat.completions.create
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=150
                )
                answer = response.choices[0].message.content.strip()
                st.subheader("Ответ:")
                st.write(answer)
            except Exception as e:
                st.error(f"Произошла ошибка: {e}")
    else:
        st.warning("Пожалуйста, введите запрос перед отправкой.")
