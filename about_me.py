import streamlit as st 

from forms.contact import contact_form 

@st.experimental_dialog("Contact Me")
def show_contact_form():
	contact_form()

#------Hero Section----------
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
	st.image("./assets/profile_image.png", width=230)


with col2:
	st.title("CaleekalAI",  anchor=False)
	st.write("Agent of Artificial Intelligence and Generative AI")

	if st.button("Contact Me"):
		show_contact_form()


# -------Tasks------------------

st.subheader("AIAgent Tasks", anchor=false)
st.write(
  """
  	- Youtube videos to Articles
  	- Toutube Videos Summary
  	


  """
)
