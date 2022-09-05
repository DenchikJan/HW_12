import json


class Candidates:

    def __init__(self, path):
        """
        Читаем json файл
        """
        with open(path, 'r', encoding="utf-8") as file:
            raw_content = file.read()
            content = json.loads(raw_content)
            self.content = content

    def get_candidate(self, candidate_id):
        candidates = self.content
        for candidate in candidates:
            if candidate['id'] == candidate_id:
                return candidate

    def get_candidates_by_name(self, candidate_name):
        candidates_name = []
        candidates = self.content
        for candidate in candidates:
            if candidate_name.lower() in candidate['name'].lower():
                candidates_name.append(candidate)
        return candidates_name

    def get_candidates_by_skill(self, skill_name):
        candidates_skill = []
        candidates = self.content
        for candidate in candidates:
            if skill_name.lower() in candidate['skills'].lower().split(', '):
                candidates_skill.append(candidate)
        return candidates_skill
