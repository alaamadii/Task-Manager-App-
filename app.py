import streamlit as st
import pandas as pd
import database as db
import utils
from datetime import datetime

def main():
    st.set_page_config(page_title="Task Manager", layout="centered")
    
    st.title("📝 Task Manager App")
    
    menu = ["Add", "View", "Update", "Delete"]
    choice = st.sidebar.selectbox("Navigation", menu)
    
    if choice == "Add":
        st.subheader("Add New Task")
        with st.form(key="add_task_form"):
            col1, col2 = st.columns(2)
            with col1:
                title = st.text_input("Task Title *")
            with col2:
                status = st.selectbox("Status", ["To Do", "In Progress", "Done"])
                due_date = st.date_input("Due Date")
                
            description = st.text_area("Task Description")
            submit_button = st.form_submit_button(label="Add Task")
            
            if submit_button:
                if not title.strip():
                    st.error("⚠️ Task Title cannot be empty. Please enter a valid title.")
                else:
                   
                    due_date_str = due_date.strftime("%Y-%m-%d")
    
           
                    if not utils.validate_date(due_date_str):
                        st.error("⚠️ Invalid Due Date format.")
                    else:
                        try:
                            db.add_task(title, description, due_date_str, status)
                            st.success(f"✅ Task '{title}' has been added successfully!")
            
                        except Exception as e:
                            st.error(f"❌ Error adding task: {e}")
    elif choice == "View":
        st.subheader("View Tasks")
        try:
            tasks = db.view_all_tasks()
            if tasks:
                df = pd.DataFrame(tasks, columns=["ID", "Title", "Description", "Due Date", "Status"])
                
                # Filter section
                st.write("### Filter Tasks")
                status_filter = st.selectbox("Filter by Status", ["All", "To Do", "In Progress", "Done"])
                
                if status_filter != "All":
                    filtered_df = df[df["Status"] == status_filter]
                else:
                    filtered_df = df
                    
                st.dataframe(filtered_df, use_container_width=True, hide_index=True)
            else:
                st.info("No tasks found. Go to 'Add' menu to create new tasks.")
        except Exception as e:
            st.error(f"Error loading tasks: {e}")
            
    elif choice == "Update":
        st.subheader("Update an Existing Task")
        try:
            tasks = db.view_all_tasks()
            if tasks:
                df = pd.DataFrame(tasks, columns=["ID", "Title", "Description", "Due Date", "Status"])
                
                # Select task to update
                task_ids = df["ID"].tolist()
                selected_task_id = st.selectbox("Select Task ID to Update", task_ids)
                
                if selected_task_id:
                    # Get selected task data
                    task_data = df[df["ID"] == selected_task_id].iloc[0]
                    
                    with st.form(key="update_task_form"):
                        new_title = st.text_input("Update Title *", value=task_data["Title"])
                        new_status_index = ["To Do", "In Progress", "Done"].index(task_data["Status"]) if task_data["Status"] in ["To Do", "In Progress", "Done"] else 0
                        new_status = st.selectbox("Update Status", ["To Do", "In Progress", "Done"], index=new_status_index)
                        
                        # Handle parsing the existing due date
                        try:
                            existing_date = datetime.strptime(task_data["Due Date"], "%Y-%m-%d").date()
                        except (ValueError, TypeError):
                            existing_date = pd.Timestamp.today().date() # Fallback

                        new_due_date = st.date_input("Update Due Date", value=existing_date)
                        new_description = st.text_area("Update Description", value=task_data["Description"])
                        
                        update_button = st.form_submit_button(label="Update Task")
                        
                        if update_button:
                            if not new_title.strip():
                                st.error("⚠️ Task Title cannot be empty.")
                            else:
                                new_due_date_str = new_due_date.strftime("%Y-%m-%d")
                                if not utils.validate_date(new_due_date_str):
                                    st.error("⚠️ Invalid Due Date format.")
                                else:
                                    db.update_task(selected_task_id, new_title, new_description, new_due_date_str, new_status)
                                    st.success(f"✅ Task ID {selected_task_id} has been updated successfully!")
                                # It's helpful to see the updated table immediately or ask user to go to view
            else:
                st.info("No tasks to update.")
        except Exception as e:
            st.error(f"Error updating task: {e}")

    elif choice == "Delete":
        st.subheader("Delete a Task")
        try:
            tasks = db.view_all_tasks()
            if tasks:
                df = pd.DataFrame(tasks, columns=["ID", "Title", "Description", "Due Date", "Status"])
                
                selected_task_id = st.selectbox("Select Task ID to Delete", df["ID"].tolist())
                
                if selected_task_id:
                    task_title_to_delete = df[df["ID"] == selected_task_id].iloc[0]["Title"]
                    st.warning(f"Are you sure you want to delete the task: **{task_title_to_delete}**?")
                    
                    # We can use columns to layout the confirm button nicer
                    confirm_delete = st.button("Yes, Delete Task", type="primary")
                    
                    if confirm_delete:
                        db.delete_task(selected_task_id)
                        st.success(f"✅ Task **'{task_title_to_delete}'** (ID: {selected_task_id}) deleted successfully!")
            else:
                st.info("No tasks to delete.")
        except Exception as e:
            st.error(f"Error deleting task: {e}")

if __name__ == '__main__':
    main()
