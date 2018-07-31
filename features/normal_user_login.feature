Feature: User login

  Scenario: Normal user login
    Given Hệ thống có user bình thường A và pass B
    When User đi tới trang quản lý
    And User nhập username A pass B
    And User bấm nút logn
    Then User login không thành công
    And User vẫn đứng ở trang login
