import moment from "moment";

const DateConverter = (date) => {

  const addedDate = moment(date).add(5.5, 'hours');
  const convertedDate =  moment(addedDate).utc().format("Do MMMM YYYY h:mm A");
  
  return convertedDate
};

export default DateConverter;