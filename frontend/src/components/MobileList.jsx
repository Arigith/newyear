import React, { useState, useEffect } from "react";

export default function TableMobiles() {
    const [mobileList, setMobileList] = useState([""]);
    const [selectedSupplier, setSelectedSupplier] = useState("");

    async function AllMobiles() {
        const response = await fetch("http://127.0.0.1:8000/phone_details/list_all");
        const data = await response.json();
        console.log(data);
        setMobileList(data);
    }

    useEffect(() => {
        AllMobiles();
    }, []);

    function handleMobileChange(evt) {
        setSelectedSupplier(evt.target.value);
    }

    return (
        <>
        <h1></h1>
        <label>
            Mobile:
            <select value={selectedSupplier} onChange={handleMobileChange}>
                <option value="">All</option>
            </select>
        </label>
        <table>
            <tr>
                <th>Phone Picture</th>
                <th>Phone Make</th>
                <th>Phone Model</th>
                <th>Phone Price</th>
            </tr>
            {mobileList
                .filter(mobiledetails => selectedSupplier== "" || mobiledetails.phone_supplier === selectedSupplier)
                .map((mobiledetails, index) => (
                <tr key={index}>
                    <td>{mobiledetails.phone_picture}</td>
                    <td>{mobiledetails.phone_supplier}</td>
                    <td>{mobiledetails.phone_model}</td>
                    <td>{mobiledetails.phone_price}</td>
                </tr>
            ))}
        </table>
        </>
    )
}