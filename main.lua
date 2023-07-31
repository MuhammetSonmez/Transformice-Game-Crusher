data = 10
function eventLoop (datA)
    if data == 0 then 
        for i = 0, 9999
        do
            tfm.exec.addShamanObject(4,-100,-200,0,0,0,false)
        end
    else
        print(data) 
        data = data - 1
    end 
end
