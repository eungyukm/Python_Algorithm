# Decision Tree for AI Behavior

This project implements a Decision Tree to control AI behavior in game.
The AI's actions are based on the distance to the player, health, and attack availablity.

## Features

### Dynamic AI Decisions
- Attack: Player is close, and AI can attack.
- Defend: Player is close, but AI cannot attack.
- Flee: Player is far, and AI's health is low.
- Approach: Player is far, and AI's health is sufficient.

### Conditions
The AI's behavior depends on
1. distance_to_player: Is the player nearby?
2. health: Is the AI's health low?
3. can_attack: Can the AI attack?

### Actions
The AI performs one of these actions
- Attack: Engage the player.
- Defend: Take a defensive stance.
- Flee: Escape to regain health.
- Approach: Move closer to the player.

### Code
```python
class DecisionTreeNode:
    def __init__(self, question=None, true_branch=None, false_branch=None, action=None):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch
        self.action = action

    def decide(self, context):
        if self.action:
            return self.action()  # 리프 노드에서 함수 호출
        if self.question(context):
            return self.true_branch.decide(context)
        else:
            return self.false_branch.decide(context)

# 조건 함수
def is_close_to_player(context):
    return context['distance_to_player'] < 5

def can_ai_attack(context):
    return context['can_attack']

def is_low_health(context):
    return context['health'] < 20

# 행동
def attack():
    return "Attack"

def defend():
    return "Defend"

def flee():
    return "Flee"

def approach():
    return "Approach"

# 트리 구성
tree = DecisionTreeNode(
    question=is_close_to_player,
    true_branch=DecisionTreeNode(
        question=can_ai_attack,
        true_branch=DecisionTreeNode(action=attack),
        false_branch=DecisionTreeNode(action=defend),
    ),
    false_branch=DecisionTreeNode(
        question=is_low_health,
        true_branch=DecisionTreeNode(action=flee),
        false_branch=DecisionTreeNode(action=approach),
    )
)

# 테스트
context = {
    'distance_to_player': 3,
    'health': 50,
    'can_attack': True
}

decision = tree.decide(context)
print(f"AI Decision: {decision}")
```