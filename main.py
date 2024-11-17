import  streamlit as st

#----Page Setup-----



about_page = st.Page(
	page="views/about_me.py",
	title="About Me",
	icon=":material/account_circle:",
	default=True)


project_1_page = st.Page(
	page="views/sales_dashboard.py",
	title="Sales Dashboard",
	icon=":material/bar_chart:"



)

project_2_page = st.Page(
	page="views/chatbot.py",
	title="Chat Bot",
	icon=":material/smart_toy:"
	



)

#------Navigation Setup---------

pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

#pg = st.navigation(
	#	{
	#	  "Info":[about_page],
	#	  "Projects":[project_1_page, project_2_page],
	#	}

#)


#-------------------Shared on all Pages---------------
st.logo("assets/codingisfun_logo.png")
st.sidebar.text("Made with ❤️ by [CaleekalAI](https://youtube.com/@codingisfun)")
