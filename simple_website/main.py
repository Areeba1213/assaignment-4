import streamlit as st

# Page config
st.set_page_config(page_title="Little Sparkles 👧", page_icon="🧸", layout="wide")

# Sidebar navigation
st.sidebar.title("🛍️ Little Sparkles")
page = st.sidebar.radio("Go to", ["Home", "Collection", "About", "Contact"])

# Home Page
if page == "Home":
    st.markdown("<h1 style='text-align: center;'>🎀 Welcome to Little Sparkles</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Cute & Colorful Clothes for Girls</h3>", unsafe_allow_html=True)

    # Centered and smaller image
    left, center, right = st.columns([1, 2, 1])
    with center:
        st.image("image/floral dress.jpg", width=450)

    st.write("Discover a delightful collection of dresses, tops, and more — perfect for every little sparkle!")

# Collection Page
elif page == "Collection":
    st.title("🧸 Our Collection")

    products = [
        {"img": "image/frik.webp", "title": "Floral Dress", "price": "$25"},
        {"img": "image/p2.webp", "title": "Party Wear", "price": "$15"},
        {"img": "image/p3.webp", "title": "Baby Frock", "price": "$30"},
    ]

    cols = st.columns(3)

    for col, product in zip(cols, products):
        with col:
            st.image(product["img"], caption=product["title"], use_container_width=True)
            st.markdown(f"**Price:** {product['price']}")

# About Page
elif page == "About":
    st.title("👗 About Little Sparkles")

    # Add image to the About section (brand logo or a friendly picture)
    st.image("image/logo.png", width=200)  # Add your brand logo or a picture of happy kids wearing clothes

    # Section 1: Our Mission
    st.subheader("🌟 Our Mission")
    st.write("""
    At **Little Sparkles**, we aim to provide the most **comfortable, stylish**, and **affordable** clothes for young girls.  
    We believe that every little girl deserves to shine bright, and we design our clothes with this vision in mind!
    """)

    # Section 2: Why Choose Us
    st.subheader("💖 Why Choose Us?")
    st.write("""
    - **Quality First:** Only the best materials for comfort and durability.  
    - **Fashionable Designs:** Trendy styles that every little girl will love.  
    - **Affordable Prices:** Great value for stylish clothes!  
    - **Fast Shipping:** We get your order to you quickly so your little one can wear it right away!
    """)

    # Section 3: Customer Testimonial (Add this for credibility)
    st.subheader("👧 Customer Testimonials")
    st.write("""
    *“My daughter loves her new dresses from Little Sparkles! The quality is amazing, and she feels like a princess in them. Highly recommend!”*  
    — Sarah, Happy Mom
    """)

    # Section 4: Call-to-Action (optional)
    st.write("📬 **Want to hear more?** Join our newsletter for exclusive updates and offers!")
    with st.form("newsletter_form"):
        email = st.text_input("Enter your email address")
        submit_button = st.form_submit_button("Subscribe")
        if submit_button:
            st.success(f"Thank you for subscribing, {email}! You'll receive our latest updates soon. 💌")

# Contact Page
elif page == "Contact":
    st.title("📬 Contact Us")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success(f"Thanks {name}! We'll get back to you soon 💌")

