import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date

# App Title
st.title("🚀 Growth Mindset Challenge")

# Sidebar for Navigation
st.sidebar.header("📌 Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📊 Progress Tracker", "📝 Daily Challenge", "💡 Tips for Growth",
    "🎯 Goal Setting", "🤔 Self-Reflection"
])

# 🏡 Home Page
if page == "🏡 Home":
    st.title("🌟 Welcome to the Growth Mindset Challenge!")

    st.markdown("""
    #### Unlock your potential. One day at a time. 💪  
    This app will guide you on a daily journey to build a stronger, smarter, and more positive version of yourself.

    ---
    ### 🌱 Why Develop a Growth Mindset?
    - ✅ **Embrace Challenges** – Treat problems as opportunities to grow.
    - 🔁 **Learn from Mistakes** – Every mistake teaches you something new.
    - 🔥 **Stay Persistent** – Growth takes effort and time.
    - 🎉 **Celebrate Effort** – It’s not just the results, but the journey.
    - 🧠 **Stay Curious** – Keep learning, keep evolving.
    
    ---
    > 🌈 *“Your potential is endless. Keep going.”*
    """)

    st.success("💡 Start your journey today by exploring the sections on the left!")

# 📊 Progress Tracker
elif page == "📊 Progress Tracker":
    st.header("📊 Your Growth Progress")

    days = st.slider("How many days have you been practicing a Growth Mindset?", 1, 30, 5)
    effort = st.slider("How much effort do you put in (1-10)?", 1, 10, 7)

    st.session_state["days"] = days

    fig, ax = plt.subplots()
    ax.bar(["Days Practiced", "Effort Level"], [days, effort], color=["blue", "green"])
    ax.set_ylabel("Level")
    st.pyplot(fig)

# 📝 Daily Challenge
elif page == "📝 Daily Challenge":
    st.header("📝 Daily Growth Challenge")

    days = st.session_state.get("days", 1)

    challenges = [
        "🔹 Identify one mistake you made today and what you learned from it.",
        "🔹 Try something new that challenges you.",
        "🔹 Replace a negative thought with a positive one.",
        "🔹 Teach a new skill to a friend.",
        "🔹 Read about someone who overcame obstacles and got successful.",
        "🔹 Write down three things you're grateful for today.",
        "🔹 Step out of your comfort zone and do something bold.",
        "🔹 Set a small, realistic goal and accomplish it today.",
        "🔹 Avoid distractions and focus on one task at a time.",
        "🔹 Help someone else achieve their goal today.",
        "🔹 Take 10 minutes to meditate or practice mindfulness.",
        "🔹 Write a letter to your future self about your dreams and goals.",
        "🔹 Identify a habit you want to change and take the first step today."
    ]

    quotes = [
        "💪 *Every challenge is a chance to grow.*",
        "🌱 *You don’t grow when you’re comfortable.*",
        "🚀 *Small steps every day lead to big change.*",
        "🔥 *Push past your limits today.*",
        "🌟 *Believe in your ability to improve.*"
    ]

    challenge_today = challenges[(days - 1) % len(challenges)]
    quote_today = quotes[days % len(quotes)]

    st.subheader("💡 Challenge for Today")
    st.markdown(f"### {challenge_today}")
    st.markdown(f"**{quote_today}**")

    if st.checkbox("✅ I completed this challenge today!"):
        st.balloons()
        st.success("Awesome! Keep it up! 🎉")

    reflection = st.text_area("📝 How did it go? What did you learn?")
    if st.button("Save Reflection"):
        if reflection.strip():
            st.success("Reflection saved! You're doing great. 💖")
        else:
            st.warning("Please write something before saving.")

# 💡 Tips for Growth
elif page == "💡 Tips for Growth":
    st.header("💡 Daily Growth Tips")

    tips = [
        "🔥 **Learn from Feedback** – Constructive criticism helps you improve.",
        "🔥 **Be Persistent** – Hard work leads to success.",
        "🔥 **Surround Yourself with Positive People** – Learn from those with a growth mindset.",
        "🔥 **Stay Curious** – Ask questions and keep learning.",
        "🔥 **Break Big Goals into Small Steps** – Focus on progress, not perfection.",
        "🔥 **Celebrate Small Wins** – Every step forward counts!",
        "🔥 **Develop a Learning Habit** – Read books, watch tutorials, and improve every day."
    ]

    days = st.session_state.get("days", 1)
    st.markdown(f"💡 **Tip for Today:** {tips[days % len(tips)]}")

    st.markdown("---")
    st.subheader("🧠 Growth Mindset Quiz")

    questions = [
        {
            "question": "What is the key aspect of a growth mindset?",
            "options": ["Fixed ability", "Effort and learning", "Talent only"],
            "answer": "Effort and learning"
        },
        {
            "question": "How should you view challenges?",
            "options": ["Avoid them", "Embrace them as learning opportunities", "Complain about them"],
            "answer": "Embrace them as learning opportunities"
        },
        {
            "question": "What is the best way to handle mistakes?",
            "options": ["Ignore them", "Learn from them", "Blame others"],
            "answer": "Learn from them"
        },
        {
            "question": "What is an essential part of growth?",
            "options": ["Giving up quickly", "Consistent effort", "Being born smart"],
            "answer": "Consistent effort"
        },
        {
            "question": "How do you improve skills?",
            "options": ["Practice and perseverance", "Natural talent", "Luck"],
            "answer": "Practice and perseverance"
        }
    ]

    st.markdown("📝 **Answer the questions below and test your mindset!**")

    for idx, q in enumerate(questions):
        st.markdown(f"**Q{idx+1}. {q['question']}**")
        user_answer = st.radio(" ", q["options"], key=f"quiz_{idx}", label_visibility="collapsed")
        if st.button(f"✅ Submit Q{idx+1}"):
            if user_answer == q["answer"]:
                st.success("🎉 Correct! You're thinking like a growth-minded person!")
            else:
                st.error(f"❌ Oops! The correct answer is: **{q['answer']}**")
        st.markdown("---")

# 🎯 Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set Your Goals")

    goal = st.text_input("📝 Write your goal:")
    deadline = st.date_input("📅 Set a deadline:", value=date.today())

    if st.button("Save Goal"):
        if goal:
            st.success(f"🎯 Goal '{goal}' set for {deadline}!")
        else:
            st.warning("⚠️ Please enter a goal first.")

# 🤔 Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 Daily Self-Reflection")

    journal = st.text_area("📖 Write about your day, your challenges, and what you learned:")

    if st.button("Save Reflection"):
        if journal.strip():
            st.success("📝 Reflection saved! Keep learning and growing.")
        else:
            st.warning("⚠️ Please write something before saving.")

# Footer
st.markdown("---")
st.markdown("🌸 *Developed by Dureshehwar Siddiqui using Streamlit: Keep Growing!*")
