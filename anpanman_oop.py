"""
アンパンマンとバイキンマンのクラス化サンプル。

このファイルでは、以下を満たすように実装しています。
- アンパンマンのインスタンスを3つ作る
- アンパンマンとバイキンマンのインスタンスを共存させる
- 「クラス」「インスタンス」「メッセージ」などの用語を使ってコメントで解説する
"""


class Anpanman:
    # ↑「クラス」: アンパンマンという設計図。
    #    ここに「どんなデータを持つか」「どんなふるまいをするか」を定義する。

    def __init__(self, name: str, power: int) -> None:
        # ↑ コンストラクタ: インスタンス生成時に最初に呼ばれる。
        # 「インスタンス」: クラス(設計図)から作られた実体。
        self.name = name
        self.power = power

    def greet(self) -> str:
        # ↑ このメソッドは、インスタンスに送る「メッセージ」の1つ。
        # 例: hero.greet() は「挨拶して」というメッセージを送っているイメージ。
        return f"ぼくは{self.name}！元気{self.power}でパトロール中！"

    def share_face(self, friend: str) -> str:
        # ↑ これもメッセージ。困っている相手に顔を分ける行動を表す。
        self.power -= 10
        return f"{friend}に顔を分けた。{self.name}の元気は{self.power}になった。"


class Baikinman:
    # ↑「クラス」: バイキンマンという別の設計図。
    #    アンパンマンとは別クラスなので、違うデータやメソッドを持てる。

    def __init__(self, plan: str) -> None:
        # インスタンスごとに作戦(plan)を持つ。
        self.plan = plan

    def shout(self) -> str:
        # インスタンスに shout() というメッセージを送ると、この処理が動く。
        return f"ハヒフヘホー！今日の作戦は『{self.plan}』だ！"


if __name__ == "__main__":
    # --- インスタンス生成エリア ---
    # 要件1: アンパンマンの数を3つにする
    anpanman_1 = Anpanman("アンパンマンA", 100)
    anpanman_2 = Anpanman("アンパンマンB", 95)
    anpanman_3 = Anpanman("アンパンマンC", 90)

    # 要件2: アンパンマンとバイキンマンのインスタンスを共存させる
    baikinman = Baikinman("アンパン工場にいたずらする")

    # --- メッセージ送信(メソッド呼び出し)エリア ---
    print(anpanman_1.greet())
    print(anpanman_2.greet())
    print(anpanman_3.greet())
    print(baikinman.shout())
    print(anpanman_1.share_face("おなかがすいた子"))
