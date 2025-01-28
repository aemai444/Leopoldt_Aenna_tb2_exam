import streamlit as st
from hugchat.login import Login
from hugchat import hugchat
import webbrowser

def main_page():
    st.title("SupportCircle - A Support Hub for Women & FLINTA Person")
    st.subheader("Find Help, Stay Safe, Take Action")

    col1, col2, = st.columns([4,1])

    # we can create tiles and place a balloon in it
    with col1:
        st.write("We are dedicated to empower women and flinta persons. This platform provides resources, guidance, and emergency support for those experiencing domestic or public violence. Here, you can find information, access local support services and help resources.")

    with col2:
        safe_exit = st.button("**🚨SAFE EXIT**")
        if safe_exit:
            webbrowser.open("https://www.google.com")

    #emergency_contacts = st.button("emergency contacts")
    #if emergency_contacts:
        #contact_page()
def checkbox_page():
    #inhalte recherchieren
    st.title("See what you can do:")

    # Create columns for layout
    col1, col2, col6 = st.columns([2,2,1])
    col3, col4 = st.columns(2)

    # Initialize session state variables for each button
    if "show_safe_night" not in st.session_state:
        st.session_state.show_safe_night = False
    if "show_day_safety" not in st.session_state:
        st.session_state.show_day_safety = False
    if "show_emergency_prep" not in st.session_state:
        st.session_state.show_emergency_prep = False
    if "show_safety_plan" not in st.session_state:
        st.session_state.show_safety_plan = False



    # Container for "Feel safer at night"
    with col1:
        with st.container():
            if st.button("Stay safe at night"):
                st.session_state.show_safe_night = not st.session_state.show_safe_night

            if st.session_state.show_safe_night:
                st.subheader("Safety Options")
                opt1 = st.checkbox("Carry pepper spray", key="night_opt1")
                opt2 = st.checkbox("Share your live location with someone", key="night_opt2")
                opt3 = st.checkbox("Keep a flashlight handy", key="night_opt3")

                if opt1 and opt2 and opt3:
                    st.success("You are prepared for the night!")

    # Container for "Stay safe during the day"
    with col2:
        with st.container():
            if st.button("Stay safe during the day"):
                st.session_state.show_day_safety = not st.session_state.show_day_safety

            if st.session_state.show_day_safety:
                st.subheader("Safety Options")
                opt4 = st.checkbox("Stay aware of your surroundings", key="day_opt1")
                opt5 = st.checkbox("Avoid secluded areas", key="day_opt2")
                opt6 = st.checkbox("Keep emergency contacts easily accessible", key="day_opt3")

                if opt4 and opt5 and opt6:
                    st.success("You are prepared for the day!")

    with col6:
        safe_exit = st.button("**🚨SAFE EXIT**")
        if safe_exit:
            webbrowser.open("https://www.google.com")

    # Container for "Emergency Preparation"
    with col3:
        with st.container():
            if st.button("Prepare for emergencies"):
                st.session_state.show_emergency_prep = not st.session_state.show_emergency_prep

            if st.session_state.show_emergency_prep:
                st.subheader("Preparation of flight kit")
                st.markdown("pack a bag with essentials in case you need to leave your home")
                opt7 = st.checkbox("money", key="emergency_opt1")
                opt8 = st.checkbox("important documents (birth certificates, passports, health insurance documents, etc.)", key="emergency_opt2")
                opt9 = st.checkbox("extra car keys", key="emergency_opt3")
                opt10 = st.checkbox("essentail items for you and your children (clothing, toiletries, medication, etc)", key="emergency_opt4")
                opt11 = st.checkbox("give it to a trusted persone", key="emergency_opt5")

                if opt7 and opt8 and opt9 and opt10 and opt11:
                    st.success("You are ready for emergencies!")

    # Container for "Travel Safety"
    with col4:
        with st.container():
            if st.button("Personal safety plan"):
                st.session_state.show_safety_plan = not st.session_state.show_travel_safety

            if st.session_state.show_safety_plan:
                st.subheader("Safety Plan for victims of domestic abuse")
                opt12 = st.checkbox("maintaain a short list of phone numbers", key="travel_opt1")
                opt13 = st.checkbox("tell 2 or 3 neighbors or friends about the violence and ask them to call the police if they hear suspicious noises", key="travel_opt2")
                opt14 = st.checkbox("make list of four places you can go and be safe", key="travel_opt3")
                opt15 = st.checkbox("", key="emergency_opt3")
                if opt12 and opt13 and opt14 and opt15:
                    st.success("You are ready for safe travel!")


def contact_page():
        st.title("Contacts")
        st.header("Need help? Find help here:")

        # Initialize session state
        if "contact_category" not in st.session_state:
            st.session_state.contact_category = False

        # Create placeholder for dynamic content
        placeholder = st.empty()

        # Create filter buttons
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
                safe_exit = st.button("**🚨SAFE EXIT**")
                if safe_exit:
                    webbrowser.open("https://www.google.com")



def AI_page():

    col1, col2 = st.columns([4,2])

    with col1:
        st.title("Your AI chatbot")
        st.write(
            "Do you have any questions that were not answered? Feel free to ask our AI assistant for more information:")

        if 'danger_count' not in st.session_state:
            st.session_state.danger_count = 0
        if 'info_count' not in st.session_state:
            st.session_state.info_count = 0

        def activate_danger():
            st.session_state.danger_count = 1
            st.session_state.info_count = 0

        def activate_info():
            st.session_state.info_count = 1
            st.session_state.danger_count = 0

        st.write("Are you in **immediate danger** or looking for **general information?**")
        c1, c2 = st.columns(2)
        with c1:
            danger_button = st.button("Immediate Danger", on_click=activate_danger)
        with c2:
            info_button = st.button("General Information", on_click=activate_info)

        @st.cache_resource
        def connect_to_hugging_face():
            hf_email = st.secrets['email']
            hf_pass = st.secrets['password']
            sign = Login(hf_email, hf_pass)
            cookies = sign.login()
            return cookies

        def generate_response(prompt):
            cookies = connect_to_hugging_face()
            chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
            return chatbot.chat(prompt)

        if st.session_state.danger_count == 1:
            if st.session_state.danger_count == 1:
                st.write("If you are in immediate danger, here are some steps you can take:")

                c1, c2, c3, c4 = st.columns(4)

                with c1:
                    call_services = st.button("Call Emergency Services")
                with c2:
                    safe_location = st.button("Find Safe Location")
                with c3:
                    contact_friend = st.button("Contact a Friend")
                with c4:
                    online_help = st.button("Online Crisis Support")

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

                st.write("Would you like further assistance?")
                prompt = st.chat_input("Enter your request")
                if prompt:
                    with st.chat_message("assistant"):
                        with st.spinner("Thinking..."):
                            response = generate_response(prompt)
                            st.write(response)

        if st.session_state.info_count == 1:
            st.write("What question do you have?")
            prompt = st.chat_input("Enter your question")
            if prompt:
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        response = generate_response(prompt)
                        st.write(response)

    with col2:
        safe_exit = st.button("**🚨SAFE EXIT**")
        if safe_exit:
            webbrowser.open("https://www.google.com")

def information_page():
    col1, col2 = st.columns([4,2])

    with col1:
        st.write(" ")
    with col2:
        safe_exit = st.button("**🚨SAFE EXIT**")
        if safe_exit:
            webbrowser.open("https://www.google.com")
    # create tabs
    tabs1, tabs2, tabs3 = st.tabs(['Women´s Shelters', 'Legal information', 'More Dogs'])

    with tabs1:
        st.header("**Procedure - The Path to a Women´s Shelter**")
        st.markdown("The path to a women's shelter is straightforward.")
        st.markdown("**Emergency hotline: 040 / 8000 4 1000**")
        st.markdown("**The emergency intake service is available day and night. We take in all women affected by violence.**")
        st.markdown("After speaking with us on the phone, a meeting point can be arranged. You can reach this meeting point using public transportation in Hamburg. From there, we will pick you up (with your children).")
        st.markdown("It is important to protect yourself and your children. In dangerous situations, call the police (Tel. 110). The police can also accompany you to the meeting point.")
        st.markdown("The emergency intake service is a safe space, and its address is confidential. You do not have to pay anything. Here, you can take some time to recover and plan your next steps.")
        st.markdown("The staff at the emergency intake will talk to you about your situation and your options. From the emergency intake, you can move directly into a women's shelter.")
        st.header("Who Can Stay in a Women's Shelter?")
        st.markdown("Any woman experiencing violence or at risk of violence can stay in a women's shelter. We welcome all women who identify as women, regardless of whether they are trans or cis, what their bodies look like, or what is stated in their documents.")
        st.header("Violence Against Women Takes Many Forms")
        st.markdown("One in four women in Germany experiences violence—for example, from their partner, family members, relatives, or other people. Many women (and their children) experience violence in their daily lives, regardless of their income, education, age, or background.")
        st.markdown("Violence comes in many different forms and is not always visible. Violence includes, for example:")
        st.markdown("- Physical violence")
        st.markdown("- Sexualized violence")
        st.markdown("- Rape")
        st.markdown("- Social Isolation")
        st.markdown("- Financial control (denying access to money)")
        st.markdown("- Human trafficking and sexual exploitation")
        st.markdown("- Deprivation of liberty")
        st.markdown("- Psychological violence (e.g., threats, demeaning behavior, control)")
        st.markdown("- Forced marriage")
        st.header("Are You Afraid That No One Will Believe You?")
        st.markdown("We are here for you. We believe you and will support you (and your children).")
        st.header("If You Can, Please Bring the Following Items:")
        st.markdown("- ID/passport/residence permit")
        st.markdown("- Health insurance card, child medical records, vaccination card, medications")
        st.markdown("- Birth certificate, marriage certificate")
        st.markdown("- Bank card and money")
        st.markdown("- Rental agreement and apartment keys")
        st.markdown("- Documents from the job center, social services, and family court")
        st.markdown("- Clothing")
        st.markdown("- School supplies and toys for the children")
        st.markdown("- Social security card")
        st.markdown("- Employment contract, pay slips")
        st.markdown("If you are missing important items, we will help you obtain them. You will receive dishes, bedding, and towels from us.")
        st.header("What is a women´s Shelter?")
        st.markdown("A women's shelter is a safe house for women who are experiencing or at risk of violence. Women with or without children (boys up to 18 years old) can stay in a women's shelter. They receive temporary accommodation, protection, counseling, and support.")
        st.markdown("Each women's shelter has rules, including keeping the address confidential. This means, for example, that residents cannot receive visitors.")
        st.markdown("At the shelter, you will live with other women and children on the same floor, sharing spaces like the kitchen, bathroom, living room, and garden. Women without children often share a room with other women. Mothers and their children usually receive their own room. You should be able to organize your daily life independently.")
        st.markdown("Only women work in the shelter, and they are committed to supporting you (and your children). This principle is called partisanship.")
        st.markdown("We do not share any information about residents with third parties. We provide counseling and support to help you lead an independent life and offer assistance in multiple languages. If needed, we work with interpreters.")
        st.markdown("For girls and boys in the women's shelter, there are staff members who help children process their experiences of violence and advocate for their well-being.")
        st.header("We Support and Assist Women and Children, for Example, With:")
        st.markdown("Processing experiences of violence")
        st.markdown("Finding new daycare or school placements")
        st.markdown("Developing new life perspectives")
        st.markdown("Clarifying financial and legal situations")
        st.markdown("Contacting and accompanying visits to authorities and offices")
        st.markdown("Searching for housing")
    with tabs2:
        st.header("**What Rights Do You Have as a Woman?**")
        st.markdown("- You have the right to leave a relationship in which violence prevails.")
        st.markdown("- You do not have to endure sexual acts against your will.")
        st.markdown("- You have the right to report your partner/husband if he has inflicted physical or sexual violence on you. (§§223/224 StGB)")
        st.markdown("- You must not be harassed or stalked.")
        st.markdown("- No one is allowed to pursue or stalk you. (§238 StGB)")
        st.markdown("- You cannot be forced into marriage against your will. (§237 StGB)")
        st.markdown("- Domestic violence and rape, even within marriage, are punishable offenses. If the police become aware of such acts, a report will automatically be filed against the perpetrator.")
        st.header("**Protection Under the Protection Against Violence Act (Gewaltschutzgesetz)**")
        st.subheader("Protection Order (Restraining Order)")
        st.markdown("The law provides protection even outside the home. You can apply for a protection order at the district court.")
        st.markdown("The court can prohibit your partner/husband from:")
        st.markdown("- Entering the residence")
        st.markdown("- Approaching you or your residence within a certain distance")
        st.markdown("- Visiting places where you regularly spend time, such as your workplace, school, kindergarten, recreational facilities, or while shopping")
        st.markdown("- Contacting you via phone, text message, letter, or email")
        st.subheader("Allocation of the Shared Residence")
        st.markdown("You can apply for an allocation of the shared residence at the district court. The court can order the violent offender to leave the shared home. This is possible even if he is the tenant or owner, although only for a limited period.")
        st.subheader("Police Eviction Order")
        st.markdown("If you call the police in the case of domestic violence, they can evict the violent man from the shared residence for up to 10 days. This is called a police eviction order. During these 10 days, you have time to decide on your next steps.")
        st.header("Further Support Options")
        st.markdown("- You can seek counseling and support from a women's advice center.")
        st.markdown("- You can consult a lawyer and apply for measures under the Protection Against Violence Act.")
        st.markdown("- If you do not feel safe despite the eviction order, you can seek shelter in a women's refuge.")
        st.write("[Click here for Information on Victim Safety](https://www.hamburg.de/resource/blob/973986/13c039e23963007e120f5f94ebe0f6b3/factsheet-opferschutz-2023-data.pdf)")
        #hinzufügen "how to recognise abuse oder sowas