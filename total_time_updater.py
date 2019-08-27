
class TotalTimeUpdater: 

    
    def updateTotal(data):

        minutes = data[0].split(":")
        hours = data[1].split(":")
        minutes[-1] = str( int(minutes[-1]) + 1  )

        hours[-1] = str (int(minutes[-1]) / 60 )
 

        minutes.insert(1,":") 
        minutes =  "".join(minutes) + "\n"
        hours.insert(1,":")
        hours = "".join(hours) + "\n"

        data[0] = minutes
        data[1] = hours

        return data
