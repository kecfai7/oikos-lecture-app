# -*- coding: utf-8 -*-
import re

with open(r'c:\Oikos Univ\generate_duo_session1.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace tags and introductions
text = text.replace('[Prof. Sarah]', '[TA Sarah]')
text = text.replace('Prof. Peter Kim & Prof. Sarah Jenkins', 'Prof. Peter Kim & TA Sarah Jenkins')
text = text.replace('Professor Sarah Jenkins (Lead Systems Engineer)', 'TA Sarah Jenkins (Smart Insight Lab AI Fellow)')
text = text.replace('Professor Sarah Jenkins and myself', 'TA Sarah Jenkins and myself')
text = text.replace('피터 킴 교수(전략/아키텍처)와 사라 젠킨스 교수(시스템/실무) 듀오 체제 출범', '피터 킴 교수(54세, 전략/비전)와 사라 조교(31세, AI 연구조교) 듀오 체제 출범')
text = text.replace('사라 교수', '사라 조교')
text = text.replace('두 교수', '피터 교수와 사라 조교')

old_s1 = "[TA Sarah] And hello everyone! I'm Professor Sarah Jenkins. We are so thrilled to co-host this journey with you. Today, we're not just going to talk about basic AI prompts or typing in search boxes. We are stepping into something far more powerful."
new_s1 = "[TA Sarah] And hello everyone! I'm Sarah Jenkins, your Teaching Assistant and AI Research Fellow at Smart Insight Lab. Professor Kim and I are so thrilled to guide you through this exciting journey! Today, we're not just going to talk about basic prompts or typing in search boxes. We are stepping into something far more powerful."
text = text.replace(old_s1, new_s1)

def fix_ta_speech(match):
    content = match.group(0)
    content = content.replace('Peter, ', 'Professor Kim, ')
    content = content.replace('Peter!', 'Professor Kim!')
    content = content.replace('Peter?', 'Professor Kim?')
    content = content.replace('Peter.', 'Professor Kim.')
    return content

text = re.sub(r'\[TA Sarah\].*?(?=\n\n|\Z)', fix_ta_speech, text, flags=re.DOTALL)

with open(r'c:\Oikos Univ\generate_duo_session1.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('generate_duo_session1.py updated to TA Sarah!')
