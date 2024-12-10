import torch
import torch.nn as nn
import torch.nn.functional as F

class ScaledDotProductAttention(nn.Module):
    def __init__(self):
        super(ScaledDotProductAttention, self).__init__()

    def forward(self, query, key, value, mask=None):
        """
        query: [batch_size, seq_len, d_k]
        key: [batch_size, seq_len, d_k]
        value: [batch_size, seq_len, d_v]
        mask: [batch_size, seq_len, seq_len] (optional)
        """
        d_k = query.size(-1)  # key dimension
        # 1. Query와 Key의 점곱
        scores = torch.matmul(query, key.transpose(-2, -1)) / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))

        # 2. Mask를 적용 (선택사항)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)

        # 3. Softmax로 확률 분포 계산
        attention_weights = F.softmax(scores, dim=-1)

        # 4. Attention 가중치를 Value에 곱하기
        output = torch.matmul(attention_weights, value)

        return output, attention_weights


# 예시: 어텐션 메커니즘 사용
if __name__ == "__main__":
    batch_size = 2
    seq_len = 4
    d_k = 8
    d_v = 8

    query = torch.rand(batch_size, seq_len, d_k)  # 랜덤 Query
    key = torch.rand(batch_size, seq_len, d_k)    # 랜덤 Key
    value = torch.rand(batch_size, seq_len, d_v)  # 랜덤 Value
    mask = None  # 필요하면 마스크를 추가 (예: 패딩 부분을 무시)

    attention = ScaledDotProductAttention()
    output, weights = attention(query, key, value, mask)

    print("Output:")
    print(output)
    print("\nAttention Weights:")
    print(weights)
