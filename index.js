$(document).ready(function () {
  datatoserver = {};

  $('input[type="file"]').change(function (e) {
    var fileName = e.target.files[0].name;
    alert('The file "' + fileName + '" has been selected.');
  });

  $(".btn").click(function () {
    var file = $('input[type="file"]').val();
    if (file == "") {
      alert("Please select a file");
    } else {
      var fileInput = document.getElementById("fileInput");
      var file = fileInput.files[0];
      var file = fileInput.files[0];
      var reader = new FileReader();
      reader.onload = function (e) {
        var data = new Uint8Array(reader.result);
        var workbook = XLSX.read(data, { type: "array" });
        var firstSheetName = workbook.SheetNames[0];
        var sheet = workbook.Sheets[firstSheetName];
        var jsonData = XLSX.utils.sheet_to_json(sheet);
        console.log(jsonData);
        //   structiure of json data
        //  [ {
        //     "DSR_BRANCH_CODE": "E04",
        //     "DSR_CNNO": "C28479305",
        //     "DSR_BOOKED_BY": "F",
        //     "DSR_CUST_CODE": "EF1529",
        //     "DSR_CN_WEIGHT": 0.7,
        //     "DSR_CN_TYPE": "AR1",
        //     "DSR_DEST": "BLR",
        //     "DSR_MODE": "AR",
        //     "DSR_NO_OF_PIECES": 1,
        //     "DSR_DEST_PIN": 560010,
        //     "DSR_BOOKING_DATE": 44986.00011574074,
        //     "DSR_AMT": 11.51,
        //     "DSR_STATUS": "B",
        //     "DSR_TRANSMF_NO": 514081656,
        //     "DSR_BOOKING_TIME": "00:10:21",
        //     "DSR_DOX": "N",
        //     "DSR_SERVICE_TAX": 0,
        //     "DSR_SPL_DISC": 0,
        //     "DSR_CONTENTS": "CLOTHING",
        //     "DSR_VALUE": 3500,
        //     "MOD_DATE": 44986.00011574074,
        //     "OFFICE_TYPE": "HO",
        //     "OFFICE_CODE": "E04",
        //     "DSR_REFNO": 124264905201,
        //     "MOD_TIME": 311,
        //     "NODEID": "MOP",
        //     "USERID": "PS02539",
        //     "TRANS_STATUS": "A",
        //     "DSR_ACT_CUST_CODE": "EO1272",
        //     "DSR_MOBILE": 9686478888,
        //     "DSR_NDX_PAPER": "N",
        //     "DSR_VOL_WEIGHT": 0,
        //     "DSR_CAPTURED_WEIGHT": 0.7,
        //     "FR_DP_CODE": "EF1529"
        // } ]

        // loop through json data

        for (let i = 0; i < jsonData.length; i++) {
          const element = jsonData[i];
          var pincode = element.DSR_DEST_PIN;
          var weight = element.DSR_CN_WEIGHT;
          var mode = element.DSR_MODE;
          datatoserver[i] = {
            pincode: pincode,
            weight: weight,
            mode: mode,
          };
        }
        console.log(datatoserver);
      };
      reader.readAsArrayBuffer(file);
      setTimeout(function () {
        sendData(datatoserver);
      }, 2000);
    }
  });
});

function sendData(datatoserver) {
  $.ajax({
    type: "POST",
    url: "http://127.0.0.1:5000/download_csv",
    data: JSON.stringify(datatoserver),
    contentType: "application/json",
    success: function (response) {
      console.log(response);
      window.location.href = "http://127.0.0.1:5000/download_file";
    },
  });
}
