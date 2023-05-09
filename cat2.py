import streamlit as st
import streamlit_book as stb
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components


def authenticate(username, password):
    users = {
        "20bce143": "maitri",
        "20bce134": "vidhi",
        "20bce160": "heni",
        "20bce128":"khushi"
    }
    if username in users and users[username] == password:
        return True
    else:
        return False

def login():
    st.title("Login Form")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate(username, password):
            st.success("Login successful!")
            st.experimental_set_query_params(login="success")
        else:
            st.error("Invalid username or password")
            st.button("Register")

            if st.button("Register"):
               st.write("h")
               
              

# Define a new function to display the content of the next page
def next_page():
    act=["Theory","Practical","Calculate","Quiz","Simulation","References"]
    ch=st.sidebar.selectbox("Select your choice",act)
    
    if ch=="Theory":
     st.title("Theory")
    
     theory = open("Theory.html")
    #  image = 'Hardwater.jpg'
    #  st.image(image, caption='Hardwater effect on tap', width=300, height=200, align='right')
     components.html(theory.read(),width=1000,height=1000)

    if ch=="Quiz":
     st.title("Quiz")
     st.subheader("Test Your Knowledge")
    
      #single choice question
     st.markdown("<h4 style='font-size:18px'>1. The alkalinity due to hydroxide ion when P > M/2 will be _____?</h4>",unsafe_allow_html=True)
     stb.single_choice("Select",options=["M-2P", "2(M-P)", "Nil", "2P-M"], answer_index=3)
     
     st.markdown("<h4 style='font-size:18px'>2. With respect to the constituents causing alkalinity in water, which of the following situation never arises?</h4>",unsafe_allow_html=True)
     stb.single_choice("Select",options=["carbonate and bicarbonate ion together", "bicarbonate and hydroxyl ion together", "hydroxyl ion only", "hydroxyl and carbonate ion together"], answer_index=1)
                
     st.markdown("<h4 style='font-size:18px'>3. What is the disadvantage of using high alkaline water?</h4>",unsafe_allow_html=True)
     stb.single_choice("Select",options=["It may lead to infections", "It may lead to electrolysis", "It may lead to caustic embrittlement", "It may lead to indigestion"], answer_index=2)

     st.markdown("<h4 style='font-size:18px'>4. What is the disadvantage of using high alkaline water?</h4>",unsafe_allow_html=True)
     stb.single_choice('Select',options=["It can cause digestive issues","It can lead to dehydration","It can lower blood pressure","D. It can improve bone health"], answer_index=0)

     st.markdown("<h4 style='font-size:18px'>5. Which of the following indicator is pink in basic medium?</h4>",unsafe_allow_html=True)
     stb.single_choice("Select",options=["Methyl orange", "Phenolphthalein", "Starch", "Litmus Paper"], answer_index=1)
    #t or f question
     
     st.markdown("<h4 style='font-size:18px'>6. The alkalinity due to carbonate ion is 2P when P > M/2.</h4>",unsafe_allow_html=True)
     stb.true_or_false("Select",answer=False)
     
     st.markdown("<h4 style='font-size:18px'>7. A water sample is not alkaline to phenolphthalein. However 100 mL of the sample, on titration with N/50 HCl, required 17.2 mL to obtain the end point, using methyl orange as indicator. What will be the alkalinity present in the sample in terms of CaCO3 equivalent ?</h4>",unsafe_allow_html=True)
     stb.single_choice("Select",options=["112 ppm", "181 ppm", "172 ppm", "79 ppm"], answer_index=2)

     st.markdown("<h4 style='font-size:18px'>8. A water sample is alkaline to both phenolphthalein and methyl orange indicators. 100 mL of this water sample required 20 mL of N/50 H2SO4 upto phenolphthalein end point. Another 100 mL of this water sample required 20 mL of N/50 H2SO4 for methyl orange indicators. Calculate the amount and type of alkalinity present in water sample.?</h4>",unsafe_allow_html=True)
     stb.single_choice("Select",options=["200 ppm", "156 ppm", "178 ppm", "146 ppm"], answer_index=0)

     st.markdown("<h4 style='font-size:18px'>9. Which of the following is true?</h4>",unsafe_allow_html=True)
     stb.single_choice("Select",options=["P=0 -> Alkalinity due to HCO3- and OH-","P=0 -> Alkalinity due to HCO3-","P=0 -> Alkalinity due to CO3-","P=0 -> Alkalinity due to CO3- and OH-"], answer_index=1)

     st.markdown("<h4 style='font-size:18px'>10. A water sample has a total alkalinity of 200 mg/L as CaCO3, and a bicarbonate alkalinity of 150 mg/L as CaCO3. What is the carbonate alkalinity of the sample?</h4>",unsafe_allow_html=True)
     stb.single_choice("Select",options=["55 ppm", "35 ppm", "75 ppm", "50 ppm"], answer_index=3)

   
    if ch=="Practical":
       st.title("Practical")
       prac = open("Practical.html")
       components.html(prac.read(),width=1000,height=1000)

     

    if ch=="Calculate":
    
      st.title('Alkalinity of Water Determination')
      st.sidebar.title('Input Parameters')

      v_acid = st.sidebar.number_input('Volume of HCl solution used (mL)', value=50.00, min_value=0.0, max_value=1000.00, step=0.1)
      c_acid = st.sidebar.number_input('Concentration of HCl solution (mol/L)', value=0.1, min_value=0.0, max_value=10.00, step=0.1)
      v_sample = st.sidebar.number_input('Volume of water sample (mL)', value=50.00, min_value=0.0, max_value=1000.00, step=0.1)

      v_na2co3 = np.array([0.00, 5.00, 10.00, 15.00, 20.00, 25.00, 30.00, 35.00, 40.00, 45.00, 50.00])
      pH = np.array([4.00, 4.30, 4.57, 4.87, 5.19, 5.55, 6.06, 6.75, 7.62, 9.06, 10.90])

      if st.button('Calculate'):

        #plot
        fig, ax = plt.subplots()
        ax.plot(v_na2co3, pH, 'bo-')
        ax.set_xlabel('Volume of Na2CO3 added (mL)')
        ax.set_ylabel('pH')
        ax.set_title('Titration Curve for Alkalinity Determination')
        st.pyplot(fig)

        v_eq = v_na2co3[np.where(pH == min(pH))]
        eq_conc = (c_acid * v_acid) / (v_sample + v_eq)
        alkalinity = eq_conc * 50000

        st.write('The alkalinity of the water sample is', alkalinity, 'mg/L')


      
      
    if ch=="Simulation":
        st.title("Simulation")
        p = open("Main_Alkalinity_Simulation (2).html")
        components.html(p.read(),width=1500,height=1500)
        
        # plot_file = open('Main_Alkalinity_Simulation (2).html','r')

        # plot = plot_file.read()

        # st.markdown(plot,unsafe_allow_html=True)

        # plot = plot_file.close()
        
        # svg_bytes = open('Simulation.svg', 'rb').read()
        # st.image(svg_bytes, format='svg')
        # st.write('')
                
        # st.header("test html import")

        # HtmlFile = open('Main_Alkalinity_Simulation.html', 'r', encoding='utf-8')
        # source_code = HtmlFile.read() 
        # print(source_code)
        # components.html(source_code) 

    if ch=="References":
        st.title("References")
        st.write('1. https://www.healthline.com/health/hard-water-hair-damage-treatment#effect-on-hair')
        st.write('2. https://www.hach.com/parameters/hardness#:~:text=Why%20Measure%20Hardness%3F%20In%20general%2C%20hard%20water%20forms,maintain%20the%20delicate%20balance%20between%20scaling%20and%20corrosivity. ')
        st.write('3. https://byjus.com/jee/hardness-of-water-types-and-removal/')


        st.write('')
  
    if st.button("Logout"):
        # Navigate to the login page in a new page when the user logs out
        st.experimental_set_query_params(logout="true")
        st.experimental_rerun()

# Main function to handle navigation between pages
def main():
    query_params = st.experimental_get_query_params()
    if "login" in query_params and query_params["login"][0] == "success":
        next_page()

    elif "logout" in query_params.values() and query_params.get("logout") == ["true"]:
        # Call a function to navigate to the login page in a new page when the user logs out
        st.experimental_set_query_params(login=None, logout=None)
        # st.experimental_rerun()
        login()
    else:
        login()

    # if "login" in st.experimental_get_query_params() and st.experimental_get_query_params()["login"][0] == "success":
    #         st.experimental_set_query_params(login=None)
    #         next_page()

if __name__ == "__main__":
    main()







# import streamlit_authenticator as stauth

# hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

# import yaml
# from yaml.loader import SafeLoader
# with open('file.yml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# mine=10
# name, authentication_status, username = authenticator.login('Login', 'main')

# if authentication_status:
#     authenticator.logout('Logout', 'main')
#     st.write(f'Welcome *{name}*')
#     st.title('Some content')
# elif authentication_status is False:
#     st.error('Username/password is incorrect')
# elif authentication_status is None:
#     st.warning('Please enter your username and password')

# if st.session_state["authentication_status"]:
#     authenticator.logout('Logout', 'main')
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     st.title('Some content')
# elif st.session_state["authentication_status"] is False:
#     st.error('Username/password is incorrect')
# elif st.session_state["authentication_status"] is None:
#     st.warning('Please enter your username and password')

# count=1
# name, authentication_status, username = authenticator.login('Login', 'main')
# if authentication_status:
#     authenticator.logout('Logout', 'main')
#     if username == 'jsmith':
#         st.write(f'Welcome *{name}*')
#         st.title('Application 1')
#     elif username == 'rbriggs':
#         st.write(f'Welcome *{name}*')
#         st.title('Application 2')
# elif authentication_status == False:
#     st.error('Username/password is incorrect')
# elif authentication_status == None:
#     st.warning('Please enter your username and password')

# if authentication_status:
#     try:
#         if authenticator.reset_password(username, 'Reset password'):
#             st.success('Password modified successfully')
#     except Exception as e:
#         st.error(e)


# try:
#     if authenticator.register_user('Register user', preauthorization=False):
#         st.success('User registered successfully')
# except Exception as e:
#     st.error(e)

# try:
#     username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
#     if username_forgot_pw:
#         st.success('New password sent securely')
#         # Random password to be transferred to user securely
#     else:
#         st.error('Username not found')
# except Exception as e:
#     st.error(e)

