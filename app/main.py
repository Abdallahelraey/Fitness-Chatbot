import streamlit as st
from src.viewers import ChatbotView
def main():
    view = ChatbotView()
    view.run()

if __name__ == "__main__":
    main()
    