import streamlit as st
import database
import api_service
from models import Product, ShoppingCart


def main():
    # --- NATIVE STREAMLIT THEME CONFIGURATION ---
    # This modifies the platform configuration natively using Python parameters
    st.config.set_option("theme.primaryColor", "#3B82F6")     # Bright accent brand color
    st.config.set_option("theme.backgroundColor", "#294D61")   # Core background canvas color
    st.config.set_option("theme.secondaryBackgroundColor", "#102A43") # Sidebar and card container background
    st.config.set_option("theme.textColor", "#E2E8F0")         # Primary reading text color

    st.set_page_config(page_title="DS Online Store", layout="wide")
    database.init_db()

    # --- Session State Management ---
    if 'role' not in st.session_state:
        st.session_state.role = None
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'cart_data' not in st.session_state:
        st.session_state.cart_data = []

        # --- Header Navigation Bar ---
    nav1, nav2 = st.columns([3, 1])
    with nav1:
        st.title("🛒 Elite Modular Python Store")
    with nav2:
        if st.session_state.role is not None:
            st.write(f"Logged in as: **{st.session_state.username}**")
            if st.button("Log Out", use_container_width=True):
                st.session_state.role = None
                st.session_state.username = None
                st.session_state.cart_data = []
                st.rerun()

    st.divider()

    # --- ACCESS PORTAL (LOGIN/REGISTER) ---
    if st.session_state.role is None:
        st.subheader("🔑 Access Portal")
        auth_tab, reg_tab = st.tabs(["Login", "Create Account"])

        with auth_tab:
            user_in = st.text_input("Username", key="login_user")
            pass_in = st.text_input("Password", type="password", key="login_pass")
            if st.button("Sign In"):
                role_found = database.verify_user(user_in, pass_in)
                if role_found:
                    st.session_state.role = role_found
                    st.session_state.username = user_in
                    st.success(f"Welcome back, {user_in}!")
                    st.rerun()
                else:
                    st.error("Invalid username or password.")

        with reg_tab:
            new_user = st.text_input("Choose Username", key="reg_user")
            new_pass = st.text_input("Choose Password", type="password", key="reg_pass")
            if st.button("Register"):
                if new_user and new_pass:
                    success = database.register_user(new_user, new_pass)
                    if success:
                        st.success("Registration complete! Please switch to the Login tab.")
                    else:
                        st.error("Username already exists.")
                else:
                    st.warning("Fields cannot be left blank.")
        return

    # --- USER MODE (SHOPPING) ---
    if st.session_state.role == 'user':
        st.sidebar.header("📦 Your Shopping Basket")
        active_cart = ShoppingCart()

        if not st.session_state.cart_data:
            st.sidebar.write("Basket is empty.")
        else:
            for item in st.session_state.cart_data:
                st.sidebar.write(f"🔹 {item['name']} — ${item['price']:.2f}")
                active_cart.add_item(Product(item['id'], item['name'], item['price']))

            subtotal = active_cart.calculate_subtotal()
            receipt = api_service.process_checkout_api(subtotal)

            st.sidebar.divider()
            st.sidebar.write(f"Subtotal: ${receipt['subtotal']:.2f}")
            st.sidebar.write(f"Tax (10%): ${receipt['tax']:.2f}")
            st.sidebar.subheader(f"Grand Total: ${receipt['final']:.2f}")

            if st.sidebar.button("Purchase Items", type="primary", use_container_width=True):
                st.balloons()
                st.sidebar.success("🎉 Thank you for purchasing!")
                st.session_state.cart_data = []
                st.button("Continue Shopping")

        st.subheader("Items Catalog")
        items = database.get_items()
        cols = st.columns(3)

        for idx, item in enumerate(items):
            with cols[idx % 3]:
                with st.container(border=True):
                    st.write(f"### {item[1]}")
                    st.subheader(f"${item[2]:.2f}")
                    if st.button("Add to Cart", key=f"add_{item[0]}"):
                        st.session_state.cart_data.append({'id': item[0], 'name': item[1], 'price': item[2]})
                        st.toast(f"Added {item[1]}!")

    # --- ADMIN MODE (CRUD + USER TABLE + GRAPH) ---
    elif st.session_state.role == 'admin':
        admin_menu = st.sidebar.radio("Navigation", ["Manage Inventory", "View Registered Users"])

        if admin_menu == "View Registered Users":
            st.header("👥 System Users Directory")
            user_list = database.get_all_users()

            table_data = []
            for u in user_list:
                table_data.append({
                    "User ID": u[0],
                    "Username": u[1],
                    "Privilege Role": u[2].upper()
                })
            st.table(table_data)

        elif admin_menu == "Manage Inventory":
            st.header("🛠 Store Inventory Override Panel")

            # Add Product Form
            with st.container(border=True):
                st.subheader("➕ Add New Product to Store")
                add_name = st.text_input("Product Name", placeholder="e.g., Wireless Mouse")
                add_price = st.number_input("Product Price ($)", min_value=0.0, value=0.0, step=0.5)
                if st.button("Create Product", type="primary"):
                    if add_name and add_price > 0:
                        database.add_new_item(add_name, add_price)
                        st.success(f"Successfully added '{add_name}' to inventory!")
                        st.rerun()
                    else:
                        st.error("Please provide a valid name and price greater than 0.")

            st.divider()

            # Live Inventory Analytics Graph
            st.subheader("📊 Inventory Price Analytics")
            raw_chart_data = database.get_chart_data()
            chart_dict = {
                "Product": [item[0] for item in raw_chart_data],
                "Price ($)": [item[1] for item in raw_chart_data]
            }
            st.bar_chart(data=chart_dict, x="Product", y="Price ($)")

            st.divider()
            st.subheader("Current Stock Items")

            # Update and Delete controls
            items = database.get_items()
            for item in items:
                with st.expander(f"Modify Item ID {item[0]}: {item[1]}"):
                    c1, c2 = st.columns(2)
                    with c1:
                        new_p = st.number_input("Update Value ($)", value=float(item[2]), key=f"val_{item[0]}")
                        if st.button("Save Price Changes", key=f"save_{item[0]}"):
                            database.update_item_price(item[0], new_p)
                            st.success("Price updated in database rows.")
                            st.rerun()
                    with c2:
                        st.write("Danger Actions")
                        if st.button("DELETE PRODUCT", key=f"del_{item[0]}", type="primary"):
                            database.delete_item(item[0])
                            st.warning("Product removed.")
                            st.rerun()


if __name__ == "__main__":
    main()