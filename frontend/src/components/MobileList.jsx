import React, { useState, useEffect } from "react";

export default function TableMobiles() {
    const [mobileList, setMobileList] = useState([""]);
    const [selectedSupplier, setSelectedSupplier] = useState("");
    const uniqueSuppliers = [...new Set(mobileList.map(mobiledetails => mobiledetails.phone_supplier))];

    async function AllMobiles() {
        try {
        const response = await fetch("http://127.0.0.1:8000/phone_details/list_all");
        const data = await response.json();
        console.log(data);
        setMobileList(data);
        } catch (error) {
            console.error(error);
        }
    }

    useEffect(() => {
        AllMobiles();
    }, []);

    function handleMobileChange(evt) {
        setSelectedSupplier(evt.target.value);
    }

    return (
        <>
        <label>
            Phone Make:
            <select value={selectedSupplier} onChange={handleMobileChange}>
                <option value="">All</option>
                {uniqueSuppliers.map(supplier => (
                    <option value={supplier}>{supplier}</option>
                ))}
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
                .filter(mobiledetails => selectedSupplier == "" || mobiledetails.phone_supplier === selectedSupplier)
                .map((mobiledetails, index) => (
                <tr key={index}>
                    <td><img src={`/images/phone_pics/${mobiledetails.phone_picture}.png`} alt="Phone Picture" style={{width: "100px", height: "auto"}} /></td>
                    <td>{mobiledetails.phone_supplier}</td>
                    <td>{mobiledetails.phone_model}</td>
                    <td>${Number(mobiledetails.phone_price).toFixed(2)}</td>
                </tr>
            ))}
        </table>
        </>
    )
}