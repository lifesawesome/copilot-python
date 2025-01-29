def fetch_vm(size):
    query = f"SELECT * FROM VMs WHERE size = '{size}'" 
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchone()

def insert_vm(size, vcpu, memory):
    query = f"INSERT INTO VMs (size, vcpu, memory) VALUES ('{size}', {vcpu}, {memory})"  
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

def update_vm(size, vcpu, memory):
    query = f"UPDATE VMs SET vcpu = {vcpu}, memory = {memory} WHERE size = '{size}'"  
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

def delete_vm(size):
    query = f"DELETE FROM VMs WHERE size = '{size}'"  
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()