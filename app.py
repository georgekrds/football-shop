import streamlit as st
import pandas as pd
import sqlite3
import create
import insert

# 1. ΡΥΘΜΙΣΕΙΣ
st.set_page_config(page_title="ΚΑΤΑΣΤΗΜΑ ΠΟΔΟΣΦΑΙΡΟΥ", page_icon="⚽", layout="wide")
if 'cart' not in st.session_state: st.session_state.cart = []
if 'mode' not in st.session_state: st.session_state.mode = 0

# 2. ΒΑΣΗ
# 2.1 ΣΥΝΔΕΣΗ
if 'conn' not in st.session_state:
    st.session_state.conn = sqlite3.connect("sport_store.db", check_same_thread=False)

def get_conn():
    return st.session_state.conn

# 2.2 ΕΚΤΕΛΕΣΗ
@st.cache_data(show_spinner=False)
def run_query(q, p=()):
    conn = get_conn()
    df = pd.read_sql(q, conn, params=p)
    df.columns = [x.upper() for x in df.columns]
    return df

def run(q, p=(), c=False):
    conn = get_conn()
    try:
        cur = conn.cursor()
        if c:
            cur.execute(q, p)
            conn.commit()
            st.cache_data.clear()
            return True
        else:
            return run_query(q, p)
    except Exception as e:
        st.error(f"Σφάλμα: {e}")
        return None

# 2.3 ΒΟΗΘΗΤΙΚΑ
def get_id(t): 
    r = run(f"SELECT IFNULL(MAX(id), 0)+1 FROM {t}")
    return int(r.iloc[0,0]) if r is not None else 1

@st.cache_data(show_spinner=False)
def get_map(t, i, n): 
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(f"SELECT {n}, {i} FROM {t}")
    return dict(cur.fetchall())

# 2.4 ΑΡΧΙΚΟΠΟΙΗΣΗ
conn = get_conn()
create.create_tables(conn)
insert.insert_initial_data(conn)

# 3. ΣΕΛΙΔΕΣ
# 3.1 ΔΙΑΧΕΙΡΙΣΗ
def page_mng():
    st.header("🛠️ ΔΙΑΧΕΙΡΙΣΗ")
    tabs = st.tabs(["ΠΕΛΑΤΕΣ", "ΠΡΟΙΟΝΤΑ", "ΠΑΡΑΓΓΕΛΙΕΣ", "ΠΩΛΗΤΕΣ", "ΚΑΤΑΣΤΗΜΑΤΑ"])

    # 3.1.1 ΠΕΛΑΤΕΣ
    with tabs[0]:
        st.dataframe(run("SELECT id, full_name, email, phone, city FROM customers ORDER BY id"), width='stretch', hide_index=True)
        st.divider(); st.subheader("ΕΙΣΑΓΩΓΗ")
        with st.form("nc"):
            c1, c2 = st.columns(2); n = c1.text_input("Όνομα *"); e = c1.text_input("Email *"); ph = c1.text_input("Τηλέφωνο *"); a = c2.text_input("Διεύθυνση *"); ci = c2.text_input("Πόλη *"); sm = get_map("salespeople","id","full_name"); s = c2.selectbox("Πωλητής", list(sm.keys())) if sm else None
            if st.form_submit_button("➕") and n and s: run("INSERT INTO customers (id, full_name, email, phone, address, city, salesperson_id) VALUES (?,?,?,?,?,?,?)", (get_id("customers"),n,e,ph,a,ci,sm[s]), c=True); st.rerun()
        st.divider(); st.subheader("ΔΙΑΓΡΑΦΗ")
        cm = get_map("customers","id","full_name"); c1, c2 = st.columns([3,1]); d = c1.selectbox("Del:", list(cm.keys()), key='dc_sel', label_visibility="collapsed") if cm else None
        if c2.button("🗑️", key='dc_btn') and d: run("DELETE FROM customers WHERE id=?", (cm[d],), c=True); st.rerun()

    # 3.1.2 ΠΡΟΪΟΝΤΑ
    with tabs[1]:
        st.dataframe(run("SELECT id, name, category, sales_price, stock_quantity, color FROM products"), width='stretch', hide_index=True)
        st.divider(); st.subheader("ΕΙΣΑΓΩΓΗ")
        with st.form("np"):
            c1, c2 = st.columns(2); n = c1.text_input("Όνομα *"); cat = c1.selectbox("Κατηγορία", ["Ένδυση", "Εξοπλισμός", "Διάφορα"]); p = c1.number_input("Τιμή", step=0.5); stck = c2.number_input("Απόθεμα", step=1); clr = c2.text_input("Χρώμα"); tm = get_map("stores","id","name"); t = c2.selectbox("Κατάστημα", list(tm.keys())) if tm else None
            if st.form_submit_button("➕") and n and t: run("INSERT INTO products (id, name, category, sales_price, stock_quantity, color, store_id) VALUES (?,?,?,?,?,?,?)", (get_id("products"),n,cat,p,stck,clr,tm[t]), c=True); st.rerun()
        st.divider(); st.subheader("ΔΙΑΓΡΑΦΗ")
        pm = get_map("products","id","name"); c1, c2 = st.columns([3,1]); dp = c1.selectbox("Del:", list(pm.keys()), key='dp_sel', label_visibility="collapsed") if pm else None
        if c2.button("🗑️", key='dp_btn') and dp: run("DELETE FROM products WHERE id=?", (pm[dp],), c=True); st.rerun()

    # 3.1.3 ΠΑΡΑΓΓΕΛΙΕΣ
    with tabs[2]:
        q_view = "SELECT o.id, o.order_date, c.full_name AS customer_name, s.full_name AS salesperson_name, o.total_amount, o.status FROM orders o JOIN customers c ON o.customer_id = c.id JOIN salespeople s ON c.salesperson_id = s.id ORDER BY o.id DESC"
        st.dataframe(run(q_view), width='stretch', hide_index=True)
        st.divider(); st.subheader("ΕΙΣΑΓΩΓΗ")
        cm = get_map("customers","id","full_name"); cust = st.selectbox("Πελάτης *", list(cm.keys())) if cm else None
        pdf = run("SELECT id, name, sales_price FROM products")
        if pdf is not None:
            popts = {r['NAME']:(r['ID'],r['SALES_PRICE']) for _,r in pdf.iterrows()}; c1,c2,c3,c4,c5 = st.columns([2,1,1,1,1]); sel = c1.selectbox("Προϊόν", list(popts.keys())); qty = c2.number_input("Ποσότητα",1,99,1); sz = c3.text_input("Μέγεθος"); clr = c4.text_input("Χρώμα")
            if c5.button("➕"): pid, pr = popts[sel]; st.session_state.cart.append({'id':pid,'name':sel,'qty':qty,'price':pr,'total':pr*qty,'size':sz,'color':clr})
        if st.session_state.cart:
            cart = pd.DataFrame(st.session_state.cart); st.dataframe(cart[["name","qty","size","color","total"]], width='stretch', hide_index=True)
            if st.button("✅ ΟΛΟΚΛΗΡΩΣΗ") and cust:
                oid = get_id("orders"); conn = get_conn(); cur = conn.cursor()
                cur.execute("INSERT INTO orders (id,status,total_amount,customer_id,order_date) VALUES (?,'Completed',?,?,DATETIME('now'))", (oid,cart['total'].sum(),cm[cust]))
                items = [(oid, i['id'], i['qty'], i['price'], i['size'], i['color']) for i in st.session_state.cart]
                cur.executemany("INSERT INTO order_items (order_id,product_id,quantity,unit_price,prod_size,color) VALUES (?,?,?,?,?,?)", items)
                conn.commit(); st.cache_data.clear(); st.session_state.cart = []; st.success("OK"); st.rerun()
            if st.button("🗑️ ΚΑΘΑΡΙΣΜΟΣ"): st.session_state.cart = []; st.rerun()
        st.divider(); st.subheader("ΔΙΑΓΡΑΦΗ")
        om = get_map("orders","id","id"); c1, c2 = st.columns([3,1]); do = c1.selectbox("Del Order:", list(om.keys()), key='do_sel', label_visibility="collapsed") if om else None
        if c2.button("🗑️", key='do_btn') and do: oid = om[do]; run("DELETE FROM order_items WHERE order_id=?", (oid,), c=True); run("DELETE FROM orders WHERE id=?", (oid,), c=True); st.rerun()

    # 3.1.4 ΠΩΛΗΤΕΣ
    with tabs[3]: st.dataframe(run("SELECT * FROM salespeople"), width='stretch', hide_index=True)
        
    # 3.1.5 ΚΑΤΑΣΤΗΜΑΤΑ
    with tabs[4]: st.dataframe(run("SELECT * FROM stores"), width='stretch', hide_index=True)

# 3.2 ΑΝΑΖΗΤΗΣΗ
def page_srch():
    st.header("🔍 ΑΝΑΖΗΤΗΣΗ")
    btns = ["ΕΡΩΤΗΣΗ 1", "ΕΡΩΤΗΣΗ 2", "ΕΡΩΤΗΣΗ 3", "ΕΡΩΤΗΣΗ 4", "ΕΡΩΤΗΣΗ 5", "ΕΡΩΤΗΣΗ 6", "ΕΡΩΤΗΣΗ 7"]
    cols = st.columns(4) + st.columns(3)
    for i, b in enumerate(btns):
        if cols[i].button(b, width='stretch'): st.session_state.mode = i + 1
    st.divider(); m = st.session_state.mode
    DATA = {
        1: ("customers", "full_name", "SELECT id, full_name, email, phone FROM customers WHERE id = ?"),
        2: ("teams", "name", "SELECT id, name, number_of_players, city FROM teams WHERE id = ?"),
        3: ("products", "name", "SELECT id, name, category, sales_price, color FROM products WHERE id = ?"),
        4: (None, None, "SELECT id, wholesale_cost, stock_quantity, name FROM products WHERE sales_price BETWEEN 3 AND 15"),
        5: (None, None, "SELECT id, full_name, city FROM customers WHERE city IN ('Starford', 'Liverpool')"),
        6: (None, None, "SELECT s.id, s.full_name, AVG(o.total_amount) AS avg_sales FROM salespeople s JOIN customers c ON s.id=c.salesperson_id JOIN orders o ON c.id=o.customer_id GROUP BY s.id,s.full_name"),
        7: (None, None, "SELECT o.id AS order_id, s.full_name AS salesperson, c.full_name AS customer, o.total_amount FROM orders o JOIN customers c ON o.customer_id = c.id JOIN salespeople s ON c.salesperson_id = s.id ORDER BY o.total_amount DESC LIMIT 1")
    }
    if m in DATA:
        tbl, col, q = DATA[m]; p = ()
        if tbl:
            opts = get_map(tbl, "id", col)
            if opts: sel = st.selectbox("Επιλογή:", list(opts.keys())); p = (opts[sel],)
        st.dataframe(run(q, p), width='stretch', hide_index=True)
    elif m == 0: st.info("ΕΠΙΛΕΞΤΕ ΕΡΩΤΗΣΗ")

# 4. ΠΛΟΗΓΗΣΗ
st.sidebar.title("⚽ ΚΑΤΑΣΤΗΜΑ ΠΟΔΟΣΦΑΙΡΟΥ")
nav = st.sidebar.radio("Πήγαινε:", ["ΔΙΑΧΕΙΡΙΣΗ", "ΑΝΑΖΗΤΗΣΗ"])
if nav == "ΔΙΑΧΕΙΡΙΣΗ": page_mng()
else: page_srch()

# 5. ΥΠΟΣΕΛΙΔΟ
st.markdown("""---
<div style='text-align: center;'><p><strong>Εργασία Εξαμήνου - Βάσεις Δεδομένων Ι</strong><br><a href='https://ionio.gr' target='_blank' style='text-decoration: none; color: #2E86C1;'>Ιόνιο Πανεπιστήμιο</a><br><br><strong>ΟΜΑΔΑ 99</strong><br>Βαν Σλότεν Σταυρούλα (inf2024025)<br>Καρύδης Γεώργιος - Εδουάρδος (inf2024072)<br>Τζώρτζη Όλγα (inf2024167)<br>Τζώρτζης Κωνσταντίνος (inf2024168)<br><br><a href='https://github.com/georgekrds/football-shop/tree/main' target='_blank' style='text-decoration: none; color: #2E86C1; display: inline-flex; align-items: center; gap: 6px;'><img src='https://upload.wikimedia.org/wikipedia/commons/c/c2/GitHub_Invertocat_Logo.svg' width='20'>GitHub Repository</a></p></div>""", unsafe_allow_html=True)
