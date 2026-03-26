import streamlit as st
st.write("Types of Animals")
# Initialize session state for info visibility and current selections
if "info_visible" not in st.session_state:
    st.session_state.info_visible = {}
if "clicked" not in st.session_state:
    st.session_state.clicked = {}
if "current_reptile" not in st.session_state:
    st.session_state.current_reptile = None
if "current_bird" not in st.session_state:
    st.session_state.current_bird = None
if "current_mammal" not in st.session_state:
    st.session_state.current_mammal = None

if "animal_type" in st.session_state:
    option = st.session_state.animal_type
    if option == "Reptiles":
        selected_reptile= st.radio("Select a Types of Reptiles", ("Snakes", "Lizards", "Turtles", "Crocodiles"))
        if selected_reptile != st.session_state.current_reptile:
            st.session_state.current_reptile = selected_reptile
            st.session_state.info_visible[selected_reptile] = True
            st.session_state.clicked[selected_reptile] = False
        if selected_reptile == "Snakes":
            if st.session_state.info_visible.get("Snakes", True):
                st.image("artifacts\\images\\snakes.png", caption="Snake")
                st.write("Snakes are legless reptiles with long, cylindrical bodies. They are carnivorous and swallow their prey whole.")
                if not st.session_state.clicked.get("Snakes", False):
                    if st.button("Thank you for the information!", key="thank_snakes"):
                        st.session_state.info_visible["Snakes"] = False
                        st.session_state.clicked["Snakes"] = True
        elif selected_reptile == "Lizards":
            if st.session_state.info_visible.get("Lizards", True):
                st.image("artifacts\\images\\lizard.png", caption="Lizard")
                st.write("Lizards are reptiles with four legs and a long tail. They are found in various habitats and can be herbivorous, insectivorous, or carnivorous.")
                if not st.session_state.clicked.get("Lizards", False):
                    if st.button("Thank you for the information!", key="thank_lizards"):
                        st.session_state.info_visible["Lizards"] = False
                        st.session_state.clicked["Lizards"] = True
        elif selected_reptile == "Turtles":
            if st.session_state.info_visible.get("Turtles", True):
                st.image("artifacts\\images\\turtle.png", caption="Turtle")
                st.write("Turtles are reptiles with a hard shell that protects their body. They are mostly herbivorous and can live in water or on land.")
                if not st.session_state.clicked.get("Turtles", False):
                    if st.button("Thank you for the information!", key="thank_turtles"):
                        st.session_state.info_visible["Turtles"] = False
                        st.session_state.clicked["Turtles"] = True
        elif selected_reptile == "Crocodiles":
            if st.session_state.info_visible.get("Crocodiles", True):
                st.image("artifacts\\images\\crocodile.png", caption="Crocodile")
                st.write("Crocodiles are large aquatic reptiles with a powerful bite. They are carnivorous and are found in tropical regions around the world.")
                if not st.session_state.clicked.get("Crocodiles", False):
                    if st.button("Thank you for the information!", key="thank_crocodiles"):
                        st.session_state.info_visible["Crocodiles"] = False
                        st.session_state.clicked["Crocodiles"] = True
    elif option == "Birds":
        selected_bird = st.radio("Select a Types of Birds", ("Eagles", "Sparrows", "Crows", "Parrots"))
        if selected_bird != st.session_state.current_bird:
            st.session_state.current_bird = selected_bird
            st.session_state.info_visible[selected_bird] = True
            st.session_state.clicked[selected_bird] = False
        if selected_bird == "Eagles":
            if st.session_state.info_visible.get("Eagles", True):
                st.image("artifacts\\images\\eagles.png", caption="Eagle")
                st.write("Eagles are large birds of prey known for their keen eyesight and powerful flight. They are carnivorous and often hunt small mammals and fish.")
                if not st.session_state.clicked.get("Eagles", False):
                    if st.button("Thank you for the information!", key="thank_eagles"):
                        st.session_state.info_visible["Eagles"] = False
                        st.session_state.clicked["Eagles"] = True
        elif selected_bird == "Sparrows":
            if st.session_state.info_visible.get("Sparrows", True):
                st.image("artifacts\\images\\sparrows.png", caption="Sparrow")
                st.write("Sparrows are small, plump birds with short tails and stubby beaks. They are often found in urban areas and feed on seeds and insects.")
                if not st.session_state.clicked.get("Sparrows", False):
                    if st.button("Thank you for the information!", key="thank_sparrows"):
                        st.session_state.info_visible["Sparrows"] = False
                        st.session_state.clicked["Sparrows"] = True
        elif selected_bird == "Crows":
            if st.session_state.info_visible.get("Crows", True):
                st.image("artifacts\\images\\crows.png", caption="Crow")
                st.write("Crows are intelligent birds known for their problem-solving skills. They are omnivorous and can adapt to various environments, often scavenging for food.")
                if not st.session_state.clicked.get("Crows", False):
                    if st.button("Thank you for the information!", key="thank_crows"):
                        st.session_state.info_visible["Crows"] = False
                        st.session_state.clicked["Crows"] = True
        elif selected_bird == "Parrots":
            if st.session_state.info_visible.get("Parrots", True):
                st.image("artifacts\\images\\parrots.png", caption="Parrot")
                st.write("Parrots are colorful birds known for their ability to mimic sounds. They are primarily herbivorous and are found in tropical and subtropical regions.")
                if not st.session_state.clicked.get("Parrots", False):
                    if st.button("Thank you for the information!", key="thank_parrots"):
                        st.session_state.info_visible["Parrots"] = False
                        st.session_state.clicked["Parrots"] = True   
    elif option == "Mammals":
        selected_mammal = st.radio("Select a Types of Mammals", ("Dogs", "Cats", "Elephants", "zebras"))
        if selected_mammal != st.session_state.current_mammal:
            st.session_state.current_mammal = selected_mammal
            st.session_state.info_visible[selected_mammal] = True
            st.session_state.clicked[selected_mammal] = False
        if selected_mammal == "Dogs":
            if st.session_state.info_visible.get("Dogs", True):
                st.image("artifacts\\images\\dogs.png", caption="Dog")
                st.write("Dogs are domesticated mammals known for their loyalty and companionship. They come in various breeds and sizes, and are often kept as pets.")
                if not st.session_state.clicked.get("Dogs", False):
                    if st.button("Thank you for the information!", key="thank_dogs"):
                        st.session_state.info_visible["Dogs"] = False
                        st.session_state.clicked["Dogs"] = True
        elif selected_mammal == "Cats":
            if st.session_state.info_visible.get("Cats", True):
                st.image("artifacts\\images\\cats.png", caption="Cat")
                st.write("Cats are small, carnivorous mammals that are often kept as pets. They are known for their agility, independence, and ability to hunt small animals.")
                if not st.session_state.clicked.get("Cats", False):
                    if st.button("Thank you for the information!", key="thank_cats"):
                        st.session_state.info_visible["Cats"] = False
                        st.session_state.clicked["Cats"] = True
        elif selected_mammal == "Elephants":
            if st.session_state.info_visible.get("Elephants", True):
                st.image("artifacts\\images\\elephants.png", caption="Elephant")
                st.write("Elephants are the largest land animals, known for their intelligence and strong social bonds. They are herbivorous and are found in Africa and Asia.")
                if not st.session_state.clicked.get("Elephants", False):
                    if st.button("Thank you for the information!", key="thank_elephants"):
                        st.session_state.info_visible["Elephants"] = False
                        st.session_state.clicked["Elephants"] = True
        elif selected_mammal == "zebras":
            if st.session_state.info_visible.get("zebras", True):
                st.image("artifacts\\images\\zebras.png", caption="Zebra")
                st.write("Zebras are African equines with distinctive black and white stripes. They are herbivorous and are found in various habitats across Africa.")
                if not st.session_state.clicked.get("zebras", False):
                    if st.button("Thank you for the information!", key="thank_zebras"):
                        st.session_state.info_visible["zebras"] = False
                        st.session_state.clicked["zebras"] = True
else:
    st.write("Please select an animal type from the main page first.")
    if st.button("Okay,Thank you!"):
            st.switch_page('app.py')