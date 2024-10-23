# input_text = Element("form_input")
# form_list = Element("form_list")

# tasks = []

# def add_form(*args):
#     # get input value
#     value = input_text.value
    
#     if value:  # 입력값이 있을 경우에만 처리
#         # create task
#         task_id = f"task-{len(tasks)}"
#         task = {
#             "id": task_id,
#             "content": value,
#         }
#         tasks.append(task)  # task 객체를 추가
        
#         task_ul = document.createElement("li")
#         task_ul.id = task["id"]
#         task_ul.innerText = task["content"]
        
#         # 삭제 버튼 생성
#         delete_button = document.createElement("button")
#         delete_button.innerText = "삭제"
#         delete_button.onclick = lambda e: remove_task(task_id)
        
#         task_ul.appendChild(delete_button)  # 삭제 버튼을 리스트 항목에 추가
#         form_list.element.appendChild(task_ul)
        
#         # 입력란 지우기
#         input_text.clear()

# def remove_task(task_id):
#     # form_list에서 항목 삭제
#     task_element = document.getElementById(task_id)
#     if task_element:
#         task_element.remove()  # DOM에서 해당 요소 제거
        
#     # tasks 리스트에서도 항목 삭제
#     global tasks
#     tasks = [task for task in tasks if task["id"] != task_id]  # task_id가 일치하지 않는 항목만 남김