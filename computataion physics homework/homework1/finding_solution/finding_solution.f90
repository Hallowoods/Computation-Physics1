program finding_solution
    integer a,b,c_,d,e
    
    do a = 1, 200, 1
        do b = a, 200
            do c_ = b,200
                do d = c_,200
                    do e = 1,200
                        if(abs(real(a,8)**5+real(b,8)**5+real(c_,8)**5+real(d,8)**5 - real(e,8)**5)<1e-5)then
                            print*,'a=',a,'b=',b,'c=',c_,'d=',d,'e=',e
                        end if
                    end do
                end do
            end do
        end do
    end do
end 


