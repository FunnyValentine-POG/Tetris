# Tetris
Mục tiêu của trò chơi là di chuyển các khối gạch đang rơi từ từ xuống trong kích thước hình chữ nhật 20 hàng x 10 cột (trên màn hình). Chỗ nào có gạch rồi thì không di chuyển được tới vị trí đó. Người chơi xếp những khối hình sao cho khối hình lấp đầy 1 hàng ngang để ghi điểm và hàng ngang ấy sẽ biến mất. <br>

Ta có hai bảng:<br>

một bảng chính gồm 24 dòng và 10 cột. Ta sẽ chỉ thể hiện ra màn hình 20 dòng còn 4 dòng kia thì không. Tại sao thế? Vì khi ta tạo 1 khối gạch mới để rơi xuống ta sẽ tạo ở khoảng 4 dòng trên cùng. Và người chơi sẽ không thấy cho đến khi nó rơi xuống dần lộ ra.<br>
một bảng Next thể hiện những khối gạch tiếp theo sẽ được cho vào màn chơi khi khối gạch hiện tại đã đặt xong.<br>
Một nhóm 4 khối sẽ rơi từ phía trên cùng của màn hình, di chuyển các khối và xoay chúng cho đến khi chúng rơi xuống phía dưới cùng của màn hình, sau đó nhóm 4 khối tiếp theo sẽ rơi xuống.<br>

Nếu để cho những khối hình cao quá màn hình, trò chơi sẽ kết thúc.<br>

Trò chơi kết thúc khi khối gạch không rơi xuống được nữa.<br>

Tất cả các Tetriminos có khả năng hoàn thành một và hai dòng. J, L có thể có ba. Chỉ có Tetrimino chữ I có khả năng để xóa bốn dòng cùng một lúc, và điều này được gọi là một “Tetris”. Xóa nhiều nhất chỉ được 4 hàng/1 lần.<br>

Phím tắt:<br>

Phím mũi tên lên: xoay khối.<br>
Phím mũi tên trái: di chuyển sang trái.<br>
Phím mũi tên phải: di chuyển sang phải.<br>
Phím mũi tên xuống: tăng tốc độ rơi.<br>

