# wordle_solver
使用最佳策略解 [wordle](https://www.nytimes.com/games/wordle/index.html) (一般模式)，保證 5 次以內解出。另外也提供自問自答。
以 salet 作為開頭，平均需要猜 3.412 次。

解法參考自
http://sonorouschocolate.com/notes/index.php?title=The_best_strategies_for_Wordle

Wordle 的題目只會出 wordle_list.txt 裡面的 2315 種單字

取自於 https://github.com/alex1770/wordle/blob/main/wordlist_hidden

## 操作說明
1. 下載 wordle_solver.py 和 wordle_list.txt，並放在同一個目錄。
<br> (不方便執行 python 程式的可以利用線上編譯器 https://www.online-python.com/)
<br> (如果不知道怎麼用的話請自立自強)
2. 執行 wordle_solver.py
3. 根據提示到 [wordle](https://www.nytimes.com/games/wordle/index.html) 作答
4. 輸入你看到的顏色的代號，預設 「012」 分別代表 「黑黃綠」

## wordle_test.py
提供 class 來做自問自答，另外也有一些對主程式做一些檢視或驗證的進階方法。

自問自答操作流程:
1. 輸入你的題目 (正確答案)
2. 開始進行作答 (你可以按一堆 Enter 洗掉上面的訊息)
3. 預設開放輸入 「?」 來作弊，它會告訴你最佳策略要猜什麼
<br> (若你沒用最佳策略作答，則策略不會更新)

<hr/>

###
有任何問題或建議，歡迎在 github 這邊或是我的 [巴哈創作](https://home.gamer.com.tw/creationDetail.php?sn=5387568) 留言。

歡迎分享。轉貼或複製程式碼，請附上本 github 網址，謝謝。
