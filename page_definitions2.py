import streamlit as st
from hugchat.login import Login
from hugchat import hugchat

# Function to display the main page
def main_page():
    #add title and subtitle
    st.title("SupportCircle - A Support Hub for Women & FLINTA*")
    st.subheader("Find Help, Stay Safe, Take Action")

    # create columns and place information inside
    col1, col2, = st.columns([4,1])

    with col1:
        # Provide an introduction to the platform
        st.write("We are dedicated to empower women and flinta*. This platform provides resources, guidance, and emergency support for those experiencing domestic violence. Here, you can find information, access local support services and help resources.")

    with col2:
        #button to safely exit the page (redirects to Google)
        url = "https://www.google.com"

        # Button zum Öffnen der Webseite
        st.link_button("**🚨Safe Exit**", url)

# Function to display checkboxes with safety plans
def checkbox_page():
    st.title("See what you can do:")
    st.subheader("Here you can find lists on what to do when you are in a abusive relationship or household")

    # Create columns for layout
    col1, col2, col3 = st.columns([2,2,1])
    col4, col5, col6 = st.columns([2,2,1])

    # Initialize session state variables for each button
    if "show_safe_night" not in st.session_state:
        st.session_state.show_safe_night = False
    if "show_safety_plan2" not in st.session_state:
        st.session_state.show_safety_plan2 = False
    if "show_emergency_prep" not in st.session_state:
        st.session_state.show_emergency_prep = False
    if "show_safety_plan" not in st.session_state:
        st.session_state.show_safety_plan = False

    # Column for "Safety Plan during relationship"
    with col1:
        # create containers for layout
        with st.container():
            with st.container():
                if st.button("Safety Plan during relationship"):
                    st.session_state.show_safety_plan = not st.session_state.show_safety_plan

                if st.session_state.show_safety_plan:
                    st.subheader("Safety Plan for victims of domestic abuse")
                    st.markdown("**During** the relationship")
                    # Checkboxes for safety actions
                    opt1 = st.checkbox("**maintain a short list of phone numbers**", key="safety_opt1")
                    opt2 = st.checkbox("**tell 2 or 3 neighbors or friends about the violence and ask them to call the police if they hear suspicious noises**", key="safety_opt2")
                    opt3 = st.checkbox("**Make list of four places you can go and be safe**", key="safety_opt3")
                    opt4 = st.checkbox("**Keep change for phone calls at all times**", key="safety_opt4")
                    opt5 = st.checkbox("**open a savings account in your name**", key="safety_opt5")
                    opt6 = st.checkbox("**Rehearse your departure** (travel from your house to your safe place several times, think up several plausible reasons for leaving at different times of the day)",key="safety_opt6")
                    st.markdown("**If you cannot leave, dial 110 and put the phone down. Dispatchers will hear what is going on in the room and will send police EVEN IF YOU DON'T TALK TO ANYBODY!**")
                    # Success message when all checkboxes are selected
                    if opt1 and opt2 and opt3 and opt4 and opt5 and opt6:
                        st.success("Now you are safer during an abusive relationship!!")


    # Column for "Safety Plan after relationship"
    with col2:
        # create containers for layout
        with st.container():
            if st.button("Safety Plan after relationship"):
                st.session_state.show_safety_plan2 = not st.session_state.show_safety_plan2

            if st.session_state.show_safety_plan2:
                st.subheader("Safety Plan for victims of domestic abuse")
                st.markdown("**After** the realtionship")
                # Checkboxes for safety actions
                opt4 = st.checkbox("**Security** (change locks, install security system, outside motion-sensitive light, etc.)", key="safety_plan2_opt1")
                opt5 = st.checkbox("**Inform your employer of your situation** (even keep a current photo of the abuser if they are not familiar enough with him to identify him)", key="safety_plan2_opt2")
                opt6 = st.checkbox("**Seek out and follow alternate routes to work and other places you go frequently**, Do not establish a predictable routine", key="safety_plan2_opt3")
                opt7 = st.checkbox("**Keep a list of emergency phone numbers handy**", key = "safety_plan2_opt4")
                opt8 = st.checkbox("**Choose some people/neighbors you trust and ask them to call the police if your ex-partner is seen near your home or your children**", key="safety_plan2_opt5")
                opt9 = st.checkbox("**Instruct the people who care for or pick up your children who is and who is not authorized to take them.**", key= "safety_plan2_opt6")
                st.markdown("**If you think he is following you drive to the closest police station. Call 110 and tell the dispatcher you are on your way. Give them a description of your car and why your are coming.**")
                # Success message when all checkboxes are selected
                if opt4 and opt5 and opt6 and opt7 and opt8 and opt9:
                    st.success("You are prepared to stay safe after ending an abusive relationship!")

    with col3:
        # button to safely exit the page (redirects to google)
        url = "https://www.google.com"

        # Button zum Öffnen der Webseite
        st.link_button("**🚨Safe Exit**", url)

    # Column for "Emergency Plan"
    with col4:
        #create containers for layout
        with st.container():
            if st.button("Prepare for emergencies"):
                st.session_state.show_emergency_prep = not st.session_state.show_emergency_prep

            if st.session_state.show_emergency_prep:
                st.subheader("Preparation of flight kit")
                st.markdown("pack a bag with essentials in case you need to leave your home")
                # Checkboxes for safety actions
                opt7 = st.checkbox("**money**", key="emergency_opt1")
                opt8 = st.checkbox("**important documents** (birth certificates, passports, health insurance documents, etc.)", key="emergency_opt2")
                opt9 = st.checkbox("**extra car keys**", key="emergency_opt3")
                opt10 = st.checkbox("**essentail items for you and your children** (clothing, toiletries, medication, etc)", key="emergency_opt4")
                opt11 = st.checkbox("**give it to a trusted person**", key="emergency_opt5")
                # Success message when all checkboxes are selected
                if opt7 and opt8 and opt9 and opt10 and opt11:
                    st.success("Great! You prepared your flight kit!")

# Function to display contact information
def contact_page():
        st.title("Contacts")
        st.header("Need help? Find help here:")

        # Initialize session state
        if "contact_category" not in st.session_state:
            st.session_state.contact_category = False

        # Create placeholder for dynamic content
        placeholder = st.empty()

        # Create columns for the layout of the page
        col1, col2, col3 = st.columns(3)

        with col1:
            support_hotlines = st.button("📞 Support Hotlines")
            if support_hotlines:
                st.session_state.contact_category = "hotlines"

        with col2:
            shelter = st.button("🏠 Find Safe Shelters")
            if shelter:
                st.session_state.contact_category = "shelters"

        with col3:
            support_services = st.button("🤝 Support Services")
            if support_services:
                st.session_state.contact_category = "services"


        # Back button to reset selection
        if st.session_state.contact_category != False:
            if st.button("🔙 Back to Overview"):
                st.session_state.contact_category = False

        # Display content based on selected category
        with placeholder.container():
            col1, col2 = st.columns([4,2])

            with col1:
                if st.session_state.contact_category == False:
                    st.subheader("Emergency Numbers:")
                    st.markdown("📞 **Police:** 110")
                    st.markdown("🚑 **Fire department/Ambulance:** 112")
                    st.markdown("📢 **Help hotline violence against women:** 116 016")
                    st.markdown("💜 **Help hotline - Sexual abuse:** 0800 22 55 530")
                    st.markdown("📞 **Telephone counselling:** 0800 111 0 111 or 0800 111 0 222")
                    st.markdown("👶 **Help hotline for children and young people:** 116 111")

                elif st.session_state.contact_category == "hotlines":
                    st.subheader("📞 Support Hotlines")
                    st.markdown("- **Violence against women:** 116 016")
                    st.markdown("- **Sexual abuse support:** 0800 22 55 530")
                    st.markdown("- **Crisis counselling:** 0800 111 0 111 or 0800 111 0 222")
                    st.markdown("- **Children & young people support:** 116 111")

                elif st.session_state.contact_category == "shelters":
                    st.subheader("🏠 Find Safe Shelters")

                    colu1, colu2 = st.columns(2)
                    with colu1:
                        st.markdown("**Women’s Shelter Lüneburg**")
                        st.markdown("Phone: 04131-61733")
                        st.markdown("Email: info@frauenhelfenfrauen-lueneburg.de")
                        st.write("[Click here for details](https://www.frauenhaus-lueneburg.de/frauenhaus-lueneburg/index.html)")

                    with colu2:
                        st.markdown("**Women´s Shelter Hamburg**")
                        st.markdown("Ermergency hotline (24/7): 040 / 8000 4 1000")
                        st.markdown("Email: schutz@24-7-frauenhaeuser-hh.de")
                        st.markdown("[Information in sign language](https://www.hilfetelefon.de/gebaerdensprache.html)")

                elif st.session_state.contact_category == "services":
                    cols1,cols2 = st.columns(2)
                    with cols1:

                        st.subheader("🤝 Support Services in Lüneburg")
                        st.markdown("**FIF counseling service for women**")
                        st.markdown("Phone: 04131-61950")
                        st.markdown("Email: info@fif-lueneburg.de")
                        st.write("[More info](https://www.frauenhaus-lueneburg.de/frauenberatungsstelle-fif/index.html)")

                        st.markdown("**BISS - Counseling & Intervention**")
                        st.markdown("Phone: 04131-2216044")
                        st.markdown("Email: info@biss-lueneburg.de")
                        st.write("[More info](https://www.frauenhaus-lueneburg.de/biss-beratung-lueneburg/index.html)")

                    with cols2:
                        st.subheader("🤝 Support Services in Hamburg")
                        st.markdown("**ISIS-Couceling service for women and girls**")
                        st.markdown("Phone: 040 –  6001 3993")
                        st.markdown("Email: beratungsstelle-isis@web.de")
                        st.write("[More info](https://beratungsstelle-isis.de/)")

                        st.markdown("**PATCHWORK - Women for Women against Violence**")
                        st.markdown("Phone: 040 – 38 61 08 43")
                        st.markdown("Email: info@patchwork-hamburg.org")
                        st.write("[More info](https://www.patchwork-hamburg.org//)")

            with col2:
                #create exits button to safely leave the page
                url = "https://www.google.com"
                
                # Button zum Öffnen der Webseite
                st.link_button("**🚨Safe Exit**", url)

def AI_page():
    # Create two columns for layout
    col1, col2 = st.columns([4,2])

    with col1:
        # Add title and description for AI chatbot
        st.title("Your AI chatbot")
        st.write(
            "Do you have any questions that were not answered? Feel free to ask our AI assistant for more information:")

        # Initialize session state variables for tracking user intent
        if 'danger_count' not in st.session_state:
            st.session_state.danger_count = 0
        if 'info_count' not in st.session_state:
            st.session_state.info_count = 0

        # Functions to update session state based on user selection
        def activate_danger():
            st.session_state.danger_count = 1
            st.session_state.info_count = 0

        def activate_info():
            st.session_state.info_count = 1
            st.session_state.danger_count = 0

        # Provide options for user to choose between emergency help or general information
        st.write("Are you in **immediate danger** or looking for **general information?**")
        c1, c2 = st.columns(2)
        with c1:
            danger_button = st.button("Immediate Danger", on_click=activate_danger)
        with c2:
            info_button = st.button("General Information", on_click=activate_info)

        # Function to connect to Hugging Face chatbot service
        @st.cache_resource
        def connect_to_hugging_face():
            hf_email = st.secrets['email']
            hf_pass = st.secrets['password']
            sign = Login(hf_email, hf_pass)
            cookies = sign.login()
            return cookies

        # Function to generate chatbot response based on user input
        def generate_response(prompt):
            cookies = connect_to_hugging_face()
            chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
            return chatbot.chat(prompt)

        # If user selects "Immediate Danger"
        if st.session_state.danger_count == 1:
            if st.session_state.danger_count == 1:
                st.write("If you are in immediate danger, here are some steps you can take:")

                # Create four columns for different emergency actions
                c1, c2, c3, c4 = st.columns(4)

                with c1:
                    call_services = st.button("Call Emergency Services")
                with c2:
                    safe_location = st.button("Find Safe Location")
                with c3:
                    contact_friend = st.button("Contact a Friend")
                with c4:
                    online_help = st.button("Online Crisis Support")

                # Display information based on user's selection
                if call_services:
                    st.write("📞 Dial 911 (or your country's emergency number) immediately.")
                    st.write("If you are unable to speak, try to text emergency services if available.")

                if safe_location:
                    st.write(
                        "🏠 Find a secure place nearby, such as a police station, hospital, or a trusted person's home.")
                    st.write("Lock doors, stay hidden if necessary, and call for help.")

                if contact_friend:
                    st.write("📲 Reach out to a trusted friend or family member.")
                    st.write("Share your location if possible and ask for assistance.")

                if online_help:
                    st.write("🌐 Consider using online crisis services or helplines in your area.")
                    st.write("Call this number: 116 016 or")
                    st.write("[Click here for crisis resources](https://www.hilfetelefon.de/)")

                # Provide additional chatbot assistance
                st.write("Would you like further assistance?")
                prompt = st.chat_input("Enter your request")
                if prompt:
                    with st.chat_message("assistant"):
                        response = generate_response(prompt)
                        st.write(response)
        # If user selects "General Information"
        if st.session_state.info_count == 1:
            st.write("What question do you have?")
            prompt = st.chat_input("Enter your question")
            if prompt:
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        response = generate_response(prompt)
                        st.write(response)
    # Column for the safe exit button
    with col2:
        url = "https://www.google.com"
        
        # Button zum Öffnen der Webseite
        st.link_button("**🚨Safe Exit**", url)

def information_page():
    # Create a two-column layout for the page
    col1, col2 = st.columns([4,2])

    with col1:
        st.write(" ")
    with col2:
        #button to safely exit page
        url = "https://www.google.com"

        # Button zum Öffnen der Webseite
        st.link_button("**🚨Safe Exit**", url)
    # create tabs
    tabs1, tabs2, tabs3 = st.tabs(['How to know', 'Legal information', 'Women´s Shelters'])

    with tabs1:
        st.header("How do you know you are in an abusive realtionship")
        st.subheader("Signs of domestic abuse")
        st.markdown(
            "If you alter your behaviour because you are frightened of how your partner will react, this could be abuse. Many women experience domestic abuse without ever being physically harmed. Remember: non-physical forms of abuse can be as destructive and as undermining as physical violence.")
        st.subheader("Spotting the signs")
        st.markdown("**Types of domestic abuse**")
        # create list of types of domestic abuse
        types_domesticabuse = [
            "**Psychological/emotional abuse:** Includes name-calling, threats and manipulation, blaming you for the abuse or ‘gaslighting’ you.",
            "**Coercive control:** When an abuser uses a pattern of behaviour over time to exert power and control. It is a criminal offence.",
            "**Physical abuse:** This isn’t only hitting. He might restrain you or throw objects. He might pinch or shove you and claim it’s a ‘joke’.",
            "**Tech abuse:** He might send abusive texts, demand access to your devices, track you with spyware, or share images of you online.",
            "**Economic abuse:** Controlling your access to money or resources. He might take your wages, stop you working, or put you in debt without your knowledge or consent",
            "**Sexual abuse:** This doesn’t have to be physical. He might manipulate, deceive or coerce you into doing things you don’t want to do."]
        for types in types_domesticabuse:
            st.markdown(f"- {types}")
        st.subheader("**Am I in an abusive relationship?**")
        st.markdown(
            "**Relationships aren’t abusive, individuals are.** Sometimes it’s tricky to know whether your experiences, or those of someone you love, qualify as abuse. We’ve come up with this list of questions to help you begin to spot the signs of an abusive partner:")
        signs_of_abuse = ["Is your partner jealous and possessive?", "Is he charming one minute and abusive the next?",
                          "Does he tell you what to wear, where to go, who to see?", "Does he constantly put you down?",
                          "Does he play mind games and make you doubt your judgement?",
                          "Does he control your money, or make sure you are dependent on him for everyday things?",
                          "Does he pressure you to have sex when you don’t want to?",
                          "Are you starting to walk on eggshells to avoid making him angry?",
                          "Does he control your access to medicine, devices or care that you need?",
                          "Does he monitor or track your movements or messages?",
                          "Does he use anger and intimidation to frighten and control you?"]
        for signs in signs_of_abuse:
            st.markdown(f"- {signs}")
        st.markdown(
            "If you answered yes to any of the above questions, then you may be experiencing domestic abuse. You don’t have to deal with this alone. Under **Contacts** you can find people and institutions that can help you.")
    with tabs2:
        st.header("**What Rights Do You Have as a Woman?**")
        # create list of legal rights
        rights = [
            "You have the right to leave a relationship in which violence prevails.",
            "You do not have to endure sexual acts against your will.",
            "You have the right to report your partner/husband if he has inflicted physical or sexual violence on you. (§§223/224 StGB)",
            "You must not be harassed or stalked. (§238 StGB)",
            "You cannot be forced into marriage against your will. (§237 StGB)",
            "Domestic violence and rape, even within marriage, are punishable offenses."]
        for right in rights:
            st.markdown(f"- {right}")
        st.header("**Protection Under the Protection Against Violence Act (Gewaltschutzgesetz)**")
        st.subheader("Protection Order (Restraining Order)")
        st.markdown("The law provides protection even outside the home. You can apply for a protection order at the district court.")
        st.markdown("The court can prohibit your partner/husband from:")
        # List of possible restrictions
        prohibition =["Entering the residence", "Approaching you or your residence within a certain distance", "visiting places where you regularly spend time, such as your workplace, school, kindergarten, recreational facilities, or while shopping", "Contacting you via phone, text message, letter, or email"]
        for p in prohibition:
            st.markdown(f"- {p}")
        st.subheader("Allocation of the Shared Residence")
        st.markdown("You can apply for an allocation of the shared residence at the district court. The court can order the violent offender to leave the shared home. This is possible even if he is the tenant or owner, although only for a limited period.")
        st.subheader("Police Eviction Order")
        st.markdown("If you call the police in the case of domestic violence, they can evict the violent man from the shared residence for up to 10 days. This is called a police eviction order. During these 10 days, you have time to decide on your next steps.")
        st.header("Further Support Options")
        #create list for additional support options available
        further_support = ["You can seek counseling and support from a women's advice center.","You can consult a lawyer and apply for measures under the Protection Against Violence Act.","If you do not feel safe despite the eviction order, you can seek shelter in a women's refuge."]
        for support in further_support:
            st.markdown(f"- {support}")
        st.markdown("- You can seek counseling and support from a women's advice center.")
        st.markdown("- You can consult a lawyer and apply for measures under the Protection Against Violence Act.")
        st.markdown("- If you do not feel safe despite the eviction order, you can seek shelter in a women's refuge.")
        st.write("[Click here for Information on Victim Safety](https://www.hamburg.de/resource/blob/973986/13c039e23963007e120f5f94ebe0f6b3/factsheet-opferschutz-2023-data.pdf)")
    with tabs3:
        st.header("**Procedure - The Path to a Women´s Shelter**")
        st.markdown("The path to a women's shelter is straightforward.")
        st.markdown("**Emergency hotline: 040 / 8000 4 1000**")
        st.markdown(
            "**The emergency intake service is available day and night. We take in all women affected by violence.**")
        st.markdown(
            "After speaking with us on the phone, a meeting point can be arranged. You can reach this meeting point using public transportation in Hamburg. From there, we will pick you up (with your children).")
        st.markdown(
            "It is important to protect yourself and your children. In dangerous situations, call the police (Tel. 110). The police can also accompany you to the meeting point.")
        st.markdown(
            "The emergency intake service is a safe space, and its address is confidential. You do not have to pay anything. Here, you can take some time to recover and plan your next steps.")
        st.markdown(
            "The staff at the emergency intake will talk to you about your situation and your options. From the emergency intake, you can move directly into a women's shelter.")
        st.header("Who Can Stay in a Women's Shelter?")
        st.markdown(
            "Any woman experiencing violence or at risk of violence can stay in a women's shelter. We welcome all women who identify as women, regardless of whether they are trans or cis, what their bodies look like, or what is stated in their documents.")
        st.header("Violence Against Women Takes Many Forms")
        # Create a list of different types of violence
        violence_types = ["Physical violence", "Sexualized violence", "Rape", "Social Isolation",
                          "Financial control (denying access to money)", "Human trafficking and sexual exploitation",
                          "Deprivation of liberty",
                          "Psychological violence (e.g., threats, demeaning behavior, control)", "Forced marriage"]
        for v in violence_types:
            st.markdown(f"- {v}")  # Display each type as a bullet point
        st.header("Are You Afraid That No One Will Believe You?")
        st.markdown("We are here for you. We believe you and will support you (and your children).")
        st.header("If You Can, Please Bring the Following Items:")
        # List of important items to bring when seeking shelter
        items_to_bring = ["ID/passport/residence permit",
                          "Health insurance card, child medical records, vaccination card, medications",
                          "Birth certificate, marriage certificate", "Bank card and money",
                          "Rental agreement and apartment keys",
                          "Documents from the job center, social services, and family court", "Clothing",
                          "School supplies and toys for the children", "Social security card",
                          "Employment contract, pay slips"]
        for item in items_to_bring:
            st.markdown(f"- {item}")
        st.markdown(
            "If you are missing important items, we will help you obtain them. You will receive dishes, bedding, and towels from us.")
        st.header("What is a women´s Shelter?")
        st.markdown(
            "A women's shelter is a safe house for women who are experiencing or at risk of violence. Women with or without children (boys up to 18 years old) can stay in a women's shelter. They receive temporary accommodation, protection, counseling, and support.")
        st.markdown(
            "Each women's shelter has rules, including keeping the address confidential. This means, for example, that residents cannot receive visitors.")
        st.markdown(
            "At the shelter, you will live with other women and children on the same floor, sharing spaces like the kitchen, bathroom, living room, and garden. Women without children often share a room with other women. Mothers and their children usually receive their own room. You should be able to organize your daily life independently.")
        st.markdown(
            "Only women work in the shelter, and they are committed to supporting you (and your children). This principle is called partisanship.")
        st.markdown(
            "We do not share any information about residents with third parties. We provide counseling and support to help you lead an independent life and offer assistance in multiple languages. If needed, we work with interpreters.")
        st.markdown(
            "For girls and boys in the women's shelter, there are staff members who help children process their experiences of violence and advocate for their well-being.")
        st.header("We Support and Assist Women and Children, for Example, With:")
        # List of support services available
        support_options = ["Processing experiences of violence", "Finding new daycare or school placements",
                           "Developing new life perspectives", "Clarifying financial and legal situations",
                           "Contacting and accompanying visits to authorities and offices", "Searching for housing"]
        for support in support_options:
            st.markdown(f"{support}")

def faq_page():
    # Set the title of the FAQ page
    st.title("FAQ - for domestic abuse")
    st.write("Click on a question to show or hide the answer.")

    # Create a two-column layout for the page
    col1, col2 = st.columns([4, 2])

    with col1:
        # List of FAQs as tuples (Question, Answer)
        faq_data = [
            ("What should I do if I am in immediate danger?",
             "If you are in immediate danger, call **110** as soon as possible. If speaking is not safe, try texting emergency services if available. You can also **leave your phone line open** so responders can listen. If you can, **find a safe place** like a neighbor’s house, a police station, or a shelter."),
            ("How can I recognize if I am in an abusive relationship?",
             "Abuse can take many forms—**physical, emotional, psychological, financial, or digital**. Some warning signs include:\n- Your partner controls who you see, what you do, or how you spend money.\n- They threaten, insult, or belittle you.\n- You feel afraid to express yourself around them.\n- They prevent you from working or talking to friends and family.\nIf you recognize these signs, know that **you are not alone, and help is available**."),
            ("How can I help a friend or family member who is being abused?",
             "- **Listen without judgment** and let them know they are not alone.\n- **Avoid pressuring them to leave**—leaving must be their decision.\n- **Provide resources** like the National Domestic Violence Hotline or local shelters.\n- **Offer practical support** like a safe place to stay or transportation.\n- **Encourage them to create a safety plan** and seek professional help."),
            ("Can domestic abuse happen without physical violence?",
             "Yes. Domestic abuse is not just **physical**—it can also be **emotional, psychological, sexual, financial, or digital**. Some examples include:\n- **Emotional abuse:** Manipulation, threats, humiliation, or gaslighting.\n- **Financial abuse:** Controlling your money, preventing you from working, or stealing from you.\n- **Digital abuse:** Monitoring your phone, online accounts, or tracking your location without consent.\n- **Sexual abuse:** Forcing or pressuring you into unwanted sexual acts.\nIf your partner **controls, manipulates, or isolates you**, it is a form of abuse, even if they haven’t hit you."),
            ("How can I keep my online activity safe if I’m planning to leave?",
             "If your abuser monitors your devices, take these precautions:\n- **Use incognito mode** or **clear browser history** after researching help.\n- **Use a safe phone or computer** at a library, work, or a friend’s place.\n- **Change passwords** for emails, bank accounts, and social media.\n- **Disable location tracking** on your phone and social apps.\n- **Create a secret email** to communicate with shelters or legal aid.\nAlways assume that **digital activity can be tracked** and take steps to stay secure.")]

        # Loop through the FAQ data and create an expandable section for each question
        for i, (question, answer) in enumerate(faq_data):
            with st.expander(question):
                st.write(answer)

    with col2:
        url = "https://www.google.com"

        # Button zum Öffnen der Webseite
        st.link_button("**🚨Safe Exit**", url)
