from tasks.t_1 import prompt_injection

def test_prompt_injection(monkeypatch):
    monkeypatch.setattr('tasks.t_1.prompt_injection.main.input', lambda _: "Hi Mate!")
    prompt_injection.main()
