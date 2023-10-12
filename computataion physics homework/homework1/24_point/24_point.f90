function calculate(num1,num2,mark)  !定义两数之间的计算,mark为运算符的记号1，2，3，4
    implicit none
    double precision :: calculate
    double precision :: num1, num2
    integer        :: mark
    !mark 有四种，分别讨论
    select case(mark)
        case (1)
            calculate = num1 + num2
        case (2)
            calculate = num1 - num2
        case (3)
            calculate = num1 * num2
        case (4)
            calculate = num1 / num2
    end select
    return
end function calculate

function find_solution(a,b,c,d)
    implicit none
    double precision,external :: calculate
    integer         :: a, b, c, d
    integer                   :: mark1, mark2, mark3
    double precision          :: res1,res2  !两个中间计算值

    double precision,external :: situationA        ! (((A·B)·C)·D)
    double precision,external :: situationB        ! ((A·(B·C))·D)
    double precision,external :: situationC        ! (A·((B·C)·D))
    double precision,external :: situationD        ! (A·(B·(C·D)))
    double precision,external :: situationE        ! ((A·B)·(C·D))
    
    integer                   :: find_solution   !储存结果
    integer                   :: found = 0
    CHARACTER                 :: mark(4)
    data                         mark / '+', '-', '*', '/' /
    
    integer                   :: i,j,k,m
    integer                   :: numlist(4)
    double precision          :: a1, a2, a3, a4

    !四个数有4种排列，下面对输入的a,b,c,d进行排列
    do i = 1, 4
        do j = 1, 4
            if(i == j) cycle
            do k = 1, 4
                if(k == i .or. k == j) cycle
                do m = 1, 4
                    if(m == i .or. m == j .or. m == k) cycle
                    numlist(i) = a
                    numlist(j) = b
                    numlist(k) = c
                    numlist(m) = d

                    a1 = DBLE(numlist(1))
                    a2 = DBLE(numlist(2))
                    a3 = DBLE(numlist(3))
                    a4 = DBLE(numlist(4))
                    !然后是算符的排列
                    do mark1 = 1, 4
                        do mark2 = 1, 4
                            do mark3 = 1, 4
                                if (abs(situationA(a1, a2, a3, a4, mark1, mark2, mark3) - DBLE(24.0)) < 1e-5) then       
                                    print *, '(((', numlist(1), mark(mark1), numlist(2), & 
                                        ')', mark(mark2), numlist(3), ')', mark(mark3), numlist(4), ')'
                                    found = 1
                                else if (abs(situationB(a1, a2, a3, a4, mark1, mark2, mark3) - DBLE(24.0)) < 1e-5) then  
                                    print *, '((', numlist(1), mark(mark1), '(', numlist(2), &
                                        mark(mark2), numlist(3), '))', mark(mark3), numlist(4), ')'
                                    found = 1
                                else if (abs(situationC(a1, a2, a3, a4, mark1, mark2, mark3) - DBLE(24.0)) < 1e-5) then  
                                    print *, '(', numlist(1), mark(mark1), '((', numlist(2), &
                                        mark(mark2), numlist(3), ')', mark(mark3), numlist(4), '))'
                                    found = 1
                                else if (abs(situationD(a1, a2, a3, a4, mark1, mark2, mark3) - DBLE(24.0)) < 1e-5) then  
                                    print *, '(', numlist(1), mark(mark1), '(', numlist(2), &
                                        mark(mark2), '(', numlist(3), mark(mark3), numlist(4), ')))'
                                    found = 1
                                else if (abs(situationE(a1, a2, a3, a4, mark1, mark2, mark3) - DBLE(24.0)) < 1e-5) then  
                                    print *, '((', numlist(1), mark(mark1), numlist(2), ')', &
                                        mark(mark2), '(', numlist(3), mark(mark3), numlist(4), '))'
                                    found = 1
                                end if
                                if (found == 1) exit
                            end do
                            if (found == 1) exit
                        end do
                        if (found == 1) exit
                    end do
                    if (found == 1) exit
                end do
                if (found == 1) exit
            end do
            if (found == 1) exit
        end do
        if (found == 1) exit
    end do

    find_solution = found
    return

end function find_solution
    
!下面针对不同的运算顺序进行函数定义，一共有五种运算顺序
! - (((A·B)·C)·D)
! - ((A·(B·C))·D)
! - (A·((B·C)·D))
! - (A·(B·(C·D)))
! - ((A·B)·(C·D))
!分别用situationA,B,C,D,E进行标记

function situationA(a, b, c, d, mark1, mark2, mark3) ! (((A·B)·C)·D)
    implicit none

    ! 函数调用
    double precision,external :: calculate

    double precision          :: situationA
    double precision          :: a, b, c, d
    integer                   :: mark1, mark2, mark3

    double precision          :: res1, res2 ! 临时存储中间两步计算过程的值

    res1 = calculate(a, b, mark1)
    res2 = calculate(res1, c, mark2)
    situationA = calculate(res2, d, mark3)
    return
end function

function situationB(a, b, c, d, mark1, mark2, mark3) ! ((A·(B·C))·D)
implicit none

    ! 函数调用
    double precision,external :: calculate

    double precision          :: situationB
    double precision          :: a, b, c, d
    integer                   :: mark1, mark2, mark3

    double precision          :: res1, res2 ! 临时存储中间两步计算过程的值

    res1 = calculate(b, c, mark2);
    res2 = calculate(a, res1, mark1);
    situationB = calculate(res2, d, mark3);

    return
end function


    
function situationC(a, b, c, d, mark1, mark2, mark3) ! (A_((B_C)_D))
    implicit none

    ! 函数调用
    double precision,external :: calculate

    double precision          :: situationC
    double precision          :: a, b, c, d
    integer                   :: mark1, mark2, mark3

    double precision          :: res1, res2 ! 临时存储中间两步计算过程的值

    res1 = calculate(b, c, mark2);
    res2 = calculate(res1, d, mark3);
    situationC = calculate(a, res2, mark1);

    return
end function


function situationD(a, b, c, d, mark1, mark2, mark3) ! (A_(B_(C_D)))
    implicit none
    double precision,external :: calculate

    double precision          :: situationD
    double precision          :: a, b, c, d
    integer                   :: mark1, mark2, mark3

    double precision          :: res1, res2 ! 临时存储中间两步计算过程的值

    res1 = calculate(c, d, mark3);
    res2 = calculate(b, res1, mark2);
    situationD = calculate(a, res2, mark1);

    return
end function


function situationE(a, b, c, d, mark1, mark2, mark3) ! ((A_B)_(C_D))
    implicit none

    ! 函数调用
    double precision,external :: calculate

    double precision          :: situationE
    double precision          :: a, b, c, d
    integer                   :: mark1, mark2, mark3

    double precision          :: res1, res2 ! 临时存储中间两步计算过程的值

    res1 = calculate(a, b, mark1);
    res2 = calculate(c, d, mark3);
    situationE = calculate(res1, res2, mark2);

    return
end function


! 最后是主函数
program point_24
    implicit none
    double precision,external :: situationA          ! (((A·B)·C)·D)
    double precision,external :: situationB         ! ((A·(B·C))·D)
    double precision,external :: situationC         ! (A·((B·C)·D))
    double precision,external :: situationD         ! (A·(B·(C·D)))
    double precision,external :: situationE         ! ((A·B)·(C·D))
    integer :: a, b, c, d
    integer :: found = 0    !标记是否找到一组解
    DOUBLE PRECISION,EXTERNAL :: calculate    
    INTEGER,EXTERNAL          :: find_solution 
    print*, 'Input 4 numbers ranging from 1 to 10:'
    read*, a,b,c,d
    found = find_solution(a, b, c, d)

    if(found == 0) then     !若没有找到解重新要求输入
        print *, "No solution for your input."
        print *, "Please try again."
    end if

end program point_24