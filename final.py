from _02_fill_sign_in_form import playbook02
from _03_go_to_courses_problems_page import playbook03
from _04_go_to_problem_page import playbook04
from time import sleep
from browser import browser

browser.get('https://ijudge.it.kmitl.ac.th')

playbook02()
playbook03()
playbook04()

sleep(10)
