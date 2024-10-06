import streamlit as st
import mysql.connector 
import time
from streamlit_option_menu import option_menu
import base64
import pandas as pd
import streamlit.components.v1 as components





mydb = mysql.connector.connect(
    host=st.secrets["mysql"]["name_host"],
    user=st.secrets["mysql"]["name_user"],
    passwd=st.secrets["mysql"]["name_passwd"],
    database=st.secrets["mysql"]["name_database"]
)

my_cursor = mydb.cursor()
st.set_page_config(page_title="Freeland", page_icon="📝", layout="wide")




def get_base64_image(image_file):
    with open(image_file, "rb") as image:
        return base64.b64encode(image.read()).decode()


image_base64 = get_base64_image("last_bng.png")
st.markdown(
    f"""
    <style>
    .main {{
        background-image: url(data:image/png;base64,{image_base64});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        color: #4a4a4a;
    }}
    .sidebar .sidebar-content {{
        background-color: rgba(248, 249, 250, 0.9);
    }}
    h1 {{
        color: #4a4a4a;
        font-family: 'Arial', sans-serif;
    }}
    .stError {{
        color: #FFFFFF; /* White text for high contrast */
        font-weight: 900; /* Extra bold */
        background-color: rgba(192, 0, 0, 0.9); /* Dark red with high opacity */
        border: 2px solid #C00000; /* Darker border */
        padding: 15px; /* More padding for better spacing */
        border-radius: 5px; /* Rounded corners */
        font-size: 18px; /* Increase font size */
    }}
    .stSuccess {{
        color: #FFFFFF; /* White text for high contrast */
        font-weight: 900; /* Extra bold */
        background-color: rgba(0, 128, 0, 0.9); /* Dark green with high opacity */
        border: 2px solid #155724; /* Darker border */
        padding: 15px; /* More padding for better spacing */
        border-radius: 5px; /* Rounded corners */
        font-size: 18px; /* Increase font size */
    }}
    .stInfo {{
        color: #FFFFFF; /* White text for high contrast */
        font-weight: 900; /* Extra bold */
        background-color: rgba(0, 123, 255, 0.9); /* Dark blue with high opacity */
        border: 2px solid #0c5460; /* Darker border */
        padding: 15px; /* More padding for better spacing */
        border-radius: 5px; /* Rounded corners */
        font-size: 18px; /* Increase font size */
        
    
    }}
    </style>
    """,
    unsafe_allow_html=True
)



st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f8ff;  /* Light blue background for sidebar */
    }
    .stSidebar > div:first-child {
        background-color: transparent;  /* Lighter blue for the top menu */
    }
    .option-menu .stButton {
        background-color: #4caf50;  /* Green button background */
        color: white;               /* White text color */
        border-radius: 5px;        /* Rounded corners */
        transition: background-color 0.3s; /* Smooth transition */
    }
    .option-menu .stButton:hover {
        background-color: #45a049;  /* Darker green on hover */
    }
    .option-menu .stButton:focus {
        outline: none;              /* Remove outline on focus */
    }
    
    </style>
    """,
    unsafe_allow_html=True
)



st.markdown(
    """
    <style>
    @media (max-width: 600px) {
        /* Adjustments for mobile devices */
        .sidebar .sidebar-content {
            padding: 10px;
            font-size: 14px; /* Smaller font size */
        }
        .stButton {
            width: 100%; /* Full width buttons */
        }
        .stTextInput {
            width: 100%; /* Full width text inputs */
        }
        h1, h2, h3 {
            font-size: 20px; /* Adjust header sizes */
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    """,
    unsafe_allow_html=True
)









st.title("")


# Initializing session state variables
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "show_sign_in" not in st.session_state:
    st.session_state["show_sign_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""








def display_footer():
    st.markdown(
        """
        <div style='position: fixed; top: 60px; right: 10px; color: gray; font-size: 13px;'>
            Developed by <strong>Aykut Engür</strong>
        </div>
        """,
        unsafe_allow_html=True
    )











import streamlit as st
import time

def registration_form():
    with st.form(key="signup", clear_on_submit=True):
        st.subheader("📋 Registration Form")
        
        # User input fields
        rg_username = st.text_input("Choose a Username", key="username_input")
        rg_email = st.text_input("Enter your Email", key="email_input")
        rg_password = st.text_input("Create a Password", type="password", key="password_input")

        # Define the password criteria
        criteria = [
            "• At least 8 characters",
            "• At least one uppercase letter",
            "• At least one special character (e.g., ?@!#%+-*_.)"
        ]
        
        # Display criteria
        st.markdown(
            "<div style='font-size: 12px; color: gray;'>" + "<br>".join(criteria) + "</div>",
            unsafe_allow_html=True
        )

        # Checkbox for License & User Agreement
        agree = st.checkbox("I agree to the License & User Agreement", key="agreement_checkbox")

        # Register button
        register_button = st.form_submit_button("Register")

        if register_button:
            # Your database check logic
            my_cursor.execute("SELECT username, email FROM freeland_st_db")
            records = my_cursor.fetchall()
            usernames_list = [record[0] for record in records]
            emails_list = [record[1] for record in records]

            # Validation logic
            if not agree:
                st.markdown("<div class='stError'>You must agree to the License & User Agreement to register.</div>", unsafe_allow_html=True)
            elif rg_username == "" or rg_email == "" or rg_password == "":
                st.markdown("<div class='stError'>All fields are required</div>", unsafe_allow_html=True)
            elif rg_username in usernames_list:
                st.markdown("<div class='stError'>This username is taken, please select another username</div>", unsafe_allow_html=True)
            elif rg_email in emails_list:
                st.markdown("<div class='stError'>This email already exists, please sign in or register with a different mail</div>", unsafe_allow_html=True)
            elif not (rg_email.endswith("@gmail.com") or rg_email.endswith("@hotmail.com") or rg_email.endswith(".com") or
                      rg_email.endswith("@yahoo.com") or rg_email.endswith("@edu.tr")):
                st.markdown("<div class='stError'>Please select a valid email address</div>", unsafe_allow_html=True)
            elif len(rg_password) < 8:
                st.markdown("<div class='stError'>The password must include at least 8 characters</div>", unsafe_allow_html=True)
            elif not any(char.isupper() for char in rg_password):
                st.markdown("<div class='stError'>The password must include at least one uppercase letter</div>", unsafe_allow_html=True)
            elif not any(char in "?@!#%+-*_%." for char in rg_password):
                st.markdown("<div class='stError'>The password must have at least one special character</div>", unsafe_allow_html=True)
            else:
                # Insert into the database
                sql = "INSERT INTO freeland_st_db (email, password, username) VALUES (%s, %s, %s)"
                values = (rg_email, rg_password, rg_username)
                my_cursor.execute(sql, values)
                mydb.commit()
                st.markdown("<div class='stSuccess'>Registration Successful! Directing to the Sign In page...</div>", unsafe_allow_html=True)
                progress_bar = st.progress(0)

                for i in range(1, 50):
                    progress_bar.progress(i)
                    time.sleep(0.04)
                st.session_state["show_sign_in"] = True  
                st.rerun()  # Refresh the app

    # Button to learn about data security
    if st.button("Learn About Data Security", key="security_info_button"):
        st.session_state["show_security_info"] = True


def security_info_page():
    st.title("Data Security Information")
    
    st.write("""
    ## Your Data is Secure

    We take your privacy seriously. Here's how we ensure your data is secure:

    - **Encryption**: All sensitive data is encrypted both in transit and at rest.
    - **Access Control**: We implement strict access controls to ensure that only authorized personnel can access your data.
    - **Regular Audits**: Our security measures are regularly audited to ensure compliance with industry standards.
    - **User Rights**: You have the right to access, modify, and delete your data at any time.

    We do not share your personal information with third parties without your consent.
    
    By using our services, you can trust that your data is well protected.
    """)

    if st.button("Back to Registration", key="back_to_registration_button"):
        st.session_state["show_security_info"] = False


# Main app logic
if 'show_security_info' not in st.session_state:
    st.session_state["show_security_info"] = False

if st.session_state["show_security_info"]:
    security_info_page()
else:
    registration_form()







def sign_in_page():
    st.subheader("🔑 Sign In")
    si_username = st.text_input("Username")
    si_password = st.text_input("Password", type="password")
    sign_in_button = st.button("Sign In")
    
    if sign_in_button:
        my_cursor.execute("SELECT * FROM freeland_st_db WHERE username = %s AND password = %s", (si_username, si_password))
        record = my_cursor.fetchone()
        if si_username == "" or si_password == "":
            st.markdown("<div class='stError'>All the areas must be filled</div>", unsafe_allow_html=True)
        elif record:
            st.session_state["authenticated"] = True
            st.session_state["username"] = si_username  # Store username in session state
            st.markdown("<div class = 'stSuccess'>Successfully signed in! Directing to the Home Page...</div>", unsafe_allow_html=True)
            progress_bar = st.progress(0)
            for i in range(1, 50):
                progress_bar.progress(i)
                time.sleep(0.04)
            st.rerun()  
        else:
            st.markdown("<div class='stError'>Incorrect username or passsword</div>", unsafe_allow_html=True)


def post_idea():
    st.subheader("💡 Post an Idea")
    topic = st.selectbox("Select a Topic", ["Sports", "Films & TV Shows", "Music & Art"])
    idea_text = st.text_area("Enter your idea here:")
    
    if st.button("Submit Idea"):
        if idea_text:
            sql = "INSERT INTO freeland_ideas_table (username, ideas, topic, created_at) VALUES (%s, %s, %s, NOW())"
            values = (st.session_state["username"], idea_text, topic)
            my_cursor.execute(sql, values)
            mydb.commit()
            st.markdown("<div class='stSuccess'>Idea posted successfully</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='stError'>Please enter an idea</div>", unsafe_allow_html=True)




def see_all_ideas():
    st.subheader("🌍 See All Ideas")
    selected_topic = st.selectbox("Choose a Topic", ["All", "Sports", "Films & TV Shows", "Music & Art"])
    
    # Modify the query to limit results to 10
    if selected_topic == "All":
        my_cursor.execute("SELECT user_id, username, ideas, created_at, likes, dislikes FROM freeland_ideas_table ORDER BY created_at DESC LIMIT 10")
    else:
        my_cursor.execute("SELECT user_id, username, ideas, created_at, likes, dislikes FROM freeland_ideas_table WHERE topic = %s ORDER BY created_at DESC LIMIT 10", (selected_topic,))
    
    ideas = my_cursor.fetchall()
    
    if ideas:
        my_cursor.execute("SELECT id FROM freeland_st_db WHERE username = %s", (st.session_state["username"],))
        user_id = my_cursor.fetchone()[0]

        for idea in ideas:
            idea_id = idea[0]
            timestamp = idea[3].strftime("%d %B %Y, %H:%M")  # Updated format
            
            # Check the user's vote on this idea
            my_cursor.execute("SELECT vote FROM user_votes WHERE user_id = %s AND idea_id = %s", (user_id, idea_id))
            user_vote = my_cursor.fetchone()

            # Display idea
            st.markdown(f"<p style='color: #58D68D;'><strong>{idea[1]}</strong>: {idea[2]} <br><em style='font-size: small; font-family: Arial;'>{timestamp}</em></p>", unsafe_allow_html=True)

            # Display like and dislike buttons in the same row
            col1, col2 = st.columns([1, 13])  
            with col1:
                
                like_button_label = f"👍 {idea[4]}"
                if user_vote and user_vote[0] == 'like':
                    like_button_label = f"❤️ {idea[4]}"

                if st.button(like_button_label, key=f"like_{idea_id}"):
                    vote_on_idea(user_id, idea_id, 'like')
                    mydb.commit()
                    st.rerun()

            with col2:
               
                dislike_button_label = f"👎 {idea[5]}"
                if user_vote and user_vote[0] == 'dislike':
                    dislike_button_label = f"💔 {idea[5]}"
                
                if st.button(dislike_button_label, key=f"dislike_{idea_id}"):
                    vote_on_idea(user_id, idea_id, 'dislike')
                    mydb.commit()
                    st.rerun()

        # Only show the message if there are more than 10 ideas available
        if len(ideas) == 10:
            st.markdown("<p style='color: green; font-size: 24px; text-align: center;'><strong>To read older posts, please visit the Filter Ideas page.</strong></p>", unsafe_allow_html=True)

    else:
        st.markdown("<p style='color: red; font-size: 24px; font-weight: bold;'>No ideas posted yet.</p>", unsafe_allow_html=True)







def vote_on_idea(user_id, idea_id, vote):
    # Check if the user has already voted on the idea
    my_cursor.execute("SELECT vote FROM user_votes WHERE user_id = %s AND idea_id = %s", (user_id, idea_id))
    existing_vote = my_cursor.fetchone()

    if existing_vote:
        if existing_vote[0] != vote:
            # If the user is changing their vote, update it
            my_cursor.execute("UPDATE user_votes SET vote = %s WHERE user_id = %s AND idea_id = %s", (vote, user_id, idea_id))
            # Update like/dislike counts
            if vote == 'like':
                my_cursor.execute("UPDATE freeland_ideas_table SET likes = likes + 1, dislikes = GREATEST(dislikes - 1, 0) WHERE user_id = %s", (idea_id,))
            elif vote == 'dislike':
                my_cursor.execute("UPDATE freeland_ideas_table SET dislikes = dislikes + 1, likes = GREATEST(likes - 1, 0) WHERE user_id = %s", (idea_id,))
        else:
            # If the same vote is clicked again, remove it (delete the vote)
            my_cursor.execute("DELETE FROM user_votes WHERE user_id = %s AND idea_id = %s", (user_id, idea_id))
            if existing_vote[0] == 'like':
                my_cursor.execute("UPDATE freeland_ideas_table SET likes = GREATEST(likes - 1, 0) WHERE user_id = %s", (idea_id,))
            else:
                my_cursor.execute("UPDATE freeland_ideas_table SET dislikes = GREATEST(dislikes - 1, 0) WHERE user_id = %s", (idea_id,))
    else:
        # Insert a new vote
        my_cursor.execute("INSERT INTO user_votes (user_id, idea_id, vote) VALUES (%s, %s, %s)", (user_id, idea_id, vote))
        if vote == 'like':
            my_cursor.execute("UPDATE freeland_ideas_table SET likes = likes + 1 WHERE user_id = %s", (idea_id,))
        elif vote == 'dislike':
            my_cursor.execute("UPDATE freeland_ideas_table SET dislikes = dislikes + 1 WHERE user_id = %s", (idea_id,))








def see_your_ideas():
    st.subheader("📝 See Your Ideas")
    
    # Fetch the latest 10 ideas from the logged-in user
    my_cursor.execute("SELECT ideas, created_at FROM freeland_ideas_table WHERE username = %s ORDER BY created_at DESC LIMIT 10", (st.session_state["username"],))
    ideas = my_cursor.fetchall()
    
    if ideas:
        for idea in ideas:
            timestamp = idea[1].strftime("%d %B %Y, %H:%M")  # Updated format
            st.markdown(f"<p style='color: #58D68D;'><strong>- {idea[0]}</strong> <br><em style='font-size: small; font-family: Arial;'>{timestamp}</em></p>", unsafe_allow_html=True)

        # If there are exactly 10 ideas, display the message to visit the filter page
        if len(ideas) == 10:
            st.markdown("<p style='color: green; font-size: 20px; text-align: center;'><strong>To read older posts, please visit the Filter Ideas page.</strong></p>", unsafe_allow_html=True)

    else:
        st.markdown("<p style='color: red; font-size: 24px; font-weight: bold;'>No ideas posted yet.</p>", unsafe_allow_html=True)

    


def delete_your_idea():
    col1, col2 = st.columns([1, 3]) 
    
    with col1:
        st.subheader("🗑️ Delete Your Idea")
        
        # Fetch the latest 10 ideas from the logged-in user
        my_cursor.execute("SELECT ideas, user_id FROM freeland_ideas_table WHERE username = %s ORDER BY created_at DESC LIMIT 10", (st.session_state["username"],))
        my_ideas = my_cursor.fetchall()
        
        if my_ideas:
            for i in my_ideas:
                st.markdown(f"<p style='color: #58D68D'><strong>- {i[0]} (IDEA NUMBER: {i[1]})</strong></p>", unsafe_allow_html=True)
        else:
            st.markdown("<span style='color:red;'>You haven't posted any ideas yet.</span>", unsafe_allow_html=True)


    

    with col1:
        selected_id_number = st.number_input(
        label="Enter the ID of the idea to delete:",
        min_value=0,
        step=1,
        format="%d",
        help="Enter the idea number you want to delete."
    )
    id_submit_button = st.button("Delete idea")
    
    if id_submit_button:
        # Check if the idea exists for the user
        my_cursor.execute("SELECT ideas FROM freeland_ideas_table WHERE user_id = %s AND username = %s", (selected_id_number, st.session_state["username"]))
        idea_check = my_cursor.fetchone()

        if idea_check:
            # Delete any votes associated with the idea
            my_cursor.execute("DELETE FROM user_votes WHERE idea_id = %s", (selected_id_number,))
            # Delete the idea itself
            my_cursor.execute("DELETE FROM freeland_ideas_table WHERE user_id = %s", (selected_id_number,))
            mydb.commit()  # Commit the changes
            st.success("Idea successfully deleted")
            time.sleep(0.7)
            st.rerun()
        else:
            st.markdown(f"<p style='color: red; font-size: 24px; font-weight: bold; text-align: center;'><strong>No idea found with ID: {selected_id_number}</strong></p>", unsafe_allow_html=True)


    if len(my_ideas) == 10:
        st.markdown("<p style='color: green; font-size: 20px; text-align: center;'><strong>To read older ideas, please visit the Filter Ideas page.</strong></p>", unsafe_allow_html=True)



    




def filter_ideas():
    global selected_user
    st.subheader("🔍 Filter Ideas")

    filter_type = st.selectbox("Select Filter Type", ["By Time", "By User"])

    if filter_type == "By User":
        # Fetch usernames from the database
        my_cursor.execute("SELECT DISTINCT username FROM freeland_ideas_table")
        users = my_cursor.fetchall()
        usernames = [user[0] for user in users]
        selected_user = st.selectbox("Select a User", usernames)

        if st.button("Filter"):
            # Fetch the latest 10 ideas for the selected user
            my_cursor.execute("SELECT ideas, created_at FROM freeland_ideas_table WHERE username = %s ORDER BY created_at DESC LIMIT 10", (selected_user,))
            ideas = my_cursor.fetchall()
            display_ideas(ideas, filter_by_user=True)

    elif filter_type == "By Time":
        selected_date = st.date_input("Select a Date", value=pd.to_datetime("today").normalize(), format="DD/MM/YYYY")

        if st.button("Filter"):
            my_cursor.execute(
                "SELECT username, ideas, created_at FROM freeland_ideas_table WHERE DATE(created_at) = %s ORDER BY created_at DESC LIMIT 10",
                (selected_date,)
            )
            ideas = my_cursor.fetchall()
            display_ideas(ideas)




def display_ideas(ideas, filter_by_user=False):
    if ideas:
        for idea in ideas:
            if filter_by_user:
                timestamp = idea[1].strftime("%d %B %Y, %H:%M")  
                st.markdown(f"<p style='color: #58D68D;'><strong>{selected_user}:</strong> {idea[0]} <br><em style='font-size: small; font-family: Arial;'>{timestamp}</em></p>", unsafe_allow_html=True)
            else:
                timestamp = idea[2].strftime("%d %B %Y, %H:%M")  
                st.markdown(f"<p style='color: #58D68D;'><strong>{idea[0]}</strong>: {idea[1]} <br><em style='font-size: small; font-family: Arial;'>{timestamp}</em></p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: red; font-size: 24px; font-weight: bold;'>No ideas found for the selected criteria.</p>", unsafe_allow_html=True)



def most_popular_ideas():
    st.subheader("🔥 Most Popular Ideas")
    my_cursor.execute("SELECT username, ideas, created_at, likes FROM freeland_ideas_table ORDER BY likes DESC LIMIT 5")
    ideas = my_cursor.fetchall()
    
    if ideas:
        for idea in ideas:
            timestamp = idea[2].strftime("%d %B %Y, %H:%M")  
            st.markdown(f"<p style='color:#58D68D;'><strong>{idea[0]}</strong>: {idea[1]} <br><em style='font-size: small; font-family: Arial;'>{timestamp} - Likes: {idea[3]}</em> </p>", unsafe_allow_html=True)

    else:   
        st.markdown("<p style='color: red; font-size: 24px; font-weight: bold;'>No popular ideas yet.</p>", unsafe_allow_html=True)





def display_about_freeland():
    st.markdown(
        """
        <div style='font-size: 24px; color: #58D68D; margin-top: 50px; text-align: center;'>  <!-- Adjust font size, color, and margin -->
        <h2 style='font-weight: bold;'>About Freeland</h2>  <!-- Bold heading -->

        <strong>Welcome to Freeland</strong>, a dynamic platform designed to foster creativity and collaboration. Our mission is to provide a space where users can share their innovative ideas, connect with like-minded individuals, and engage in meaningful discussions.

        At Freeland, we believe in the power of ideas. Whether you're passionate about sports, films, music, or art, you can post your thoughts, gather feedback, and inspire others. Users can easily like or dislike ideas, fostering a community-driven approach to innovation.

        This project was developed by <strong>Aykut Engür</strong>, a computer science student. Join us in our journey to create a vibrant community of thinkers and dreamers. Together, let’s bring new ideas to life!

        <div style='margin-top: 30px;'>
            <a href='https://www.instagram.com/freeland_app?igsh=MXVwZTFkd2JqeWJ6bQ==' target='_blank'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png' alt='Instagram' style='width: 50px; height: 50px; margin-right: 10px;'/>
            </a>
            <span style='font-size: 18px;'>Click on the icon for the latest updates and news about the app, <strong>follow us on Instagram!</strong></span>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )







def delete_message():
    st.subheader("🗑️ Delete Your Messages")

    # Fetch the latest 10 messages sent by the user
    sql = "SELECT message_id, receiver, message FROM messages WHERE sender = %s ORDER BY created_at DESC LIMIT 10"
    my_cursor.execute(sql, (st.session_state["username"],))
    messages = my_cursor.fetchall()

    if messages:
        for message in messages:
            st.markdown(f'<span style="color: #58D68D;">ID: {message[0]}, To: {message[1]}, Message: {message[2]}</span>', unsafe_allow_html=True)

        message_number = st.number_input("Select the ID of the message you want to delete", min_value=1)

        if st.button("Delete Message"):
            # Fetch all message IDs to check if the selected one exists
            my_cursor.execute("SELECT message_id FROM messages WHERE sender = %s", (st.session_state["username"],))
            message_ids_list = [i[0] for i in my_cursor.fetchall()]

            if message_number not in message_ids_list:
                st.markdown(f"<div style='color: red;'>No messages with the ID: {message_number}.</div>", unsafe_allow_html=True)
            else:
                delete_sql = "DELETE FROM messages WHERE message_id = %s AND sender = %s"
                my_cursor.execute(delete_sql, (message_number, st.session_state["username"]))
                mydb.commit()
                st.markdown("<div class='stSuccess'>Message deleted successfully!</div>", unsafe_allow_html=True)
                time.sleep(0.5)
                st.rerun()
    else:
        st.markdown("<div style='color: red;'>You have no messages to delete.</div>", unsafe_allow_html=True)









def send_message():
    st.subheader("📩 Send Message")
    
    # Fetch users who have posted at least one idea
    my_cursor.execute("SELECT DISTINCT username FROM freeland_ideas_table")
    users = my_cursor.fetchall()
    usernames = [user[0] for user in users]

    selected_user = st.selectbox("Select a User", usernames)
    message_text = st.text_area("Write your message here:")
    
    if st.button("Send Message"):
        if message_text:
            sql = "INSERT INTO messages (sender, receiver, message) VALUES (%s, %s, %s)"
            values = (st.session_state["username"], selected_user, message_text)
            my_cursor.execute(sql, values)
            mydb.commit()
            st.markdown(f"<div class='stSuccess'>Your message has been sent to {selected_user}'s inbox!</div>", unsafe_allow_html=True)
            time.sleep(0.7)
            st.rerun()
        else:
            st.markdown("<div class='stError';>Enter a text before sending a message.</div>", unsafe_allow_html=True)






def your_inbox():
    st.subheader("📬 Your Inbox")
    # Modify the query to fetch the latest 10 messages
    my_cursor.execute("SELECT sender, message, created_at FROM messages WHERE receiver = %s ORDER BY created_at DESC LIMIT 10", (st.session_state["username"],))
    messages = my_cursor.fetchall()
    
    if messages:
        for message in messages:
            timestamp = message[2].strftime("%d %B %Y, %H:%M")
            st.markdown(f"<p style='color: #58D68D;'><strong>{message[0]}:</strong> {message[1]} <br><em style='font-size: small; font-family: Arial;'>{timestamp}</em></p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: red; font-weight: bold;'>No messages in your inbox.</p>", unsafe_allow_html=True)







def home_page():
    with st.sidebar:
        st.sidebar.markdown(f"<h2 style='font-weight: bold; color: #58D68D;'>Welcome, {st.session_state['username']}!</h2>", unsafe_allow_html=True)

        selected = option_menu("Home Page", 
                       ["See All Ideas", "Post Ideas", "See Your Ideas", "Delete Your Ideas", "Filter Ideas", "Most Popular Ideas", "Contact with Freelanders", "Your Inbox", "About Freeland"],
                       icons=['eye', 'pencil', 'book', 'trash', 'filter', 'star', 'envelope', 'info'], 
                       menu_icon="cast", 
                       default_index=0,
                       styles={
                           "container": {"padding": "0!important", "background-color": "transparent"},
                           "icon": {"font-size": "20px"},  
                           "label": {"font-size": "16px", "color": "black"},  
                       })

    if selected == "See All Ideas":
        see_all_ideas()
    elif selected == "Post Ideas":
        post_idea()
    elif selected == "See Your Ideas":
        see_your_ideas()
    elif selected == "Delete Your Ideas":
        delete_your_idea()
    elif selected == "Filter Ideas":
        filter_ideas()
    elif selected == "Most Popular Ideas":
        most_popular_ideas()
    elif selected == "About Freeland":
        display_about_freeland()
    elif selected == "Contact with Freelanders":
        col1, col2 = st.columns(2)
        with col1:
            send_message()
        with col2:
            delete_message()
    elif selected == "Your Inbox":
        your_inbox() 
    
    st.sidebar.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

    if st.sidebar.button("Logout"):
        st.markdown("<div class='stInfo'>Logging out...</div>", unsafe_allow_html=True)
        time.sleep(0.8)
        st.session_state["authenticated"] = False
        st.session_state["show_sign_in"] = False
        st.rerun()

    display_footer()


# Main logic
if st.session_state["authenticated"]:
    home_page()
else:
    if st.session_state["show_sign_in"]:
        sign_in_page()
        display_footer()
    else:
        option = st.selectbox("Choose an option", ["Sign In", "Register"], 
                               format_func=lambda x: f"{x}", 
                               help="Select to either sign in or register.")
        if option == "Sign In":
            sign_in_page()
            display_footer()
        elif option == "Register":
            registration_form()
            display_footer()
            
            