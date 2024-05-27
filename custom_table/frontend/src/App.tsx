import { useState, useEffect } from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { ProductService } from './service';
import { Streamlit, withStreamlitConnection, ComponentProps } from "streamlit-component-lib"

interface Product {
    id: string;
    code: string;
    name: string;
    description: string;
    image: string;
    price: number;
    category: string;
    quantity: number;
    inventoryStatus: string;
    rating: number;
    [key: string]: any
}

interface ColumnMeta {
    field: string;
    header: string;
}


function ReorderDemo({ args }: ComponentProps) {

    const [dataJson, setDataJson] = useState<any[]>([]);
    const [columnsJson, setcColumnsJson] = useState<ColumnMeta[]>([]);

    useEffect(() => {
        const obj = JSON.parse(args.html)
        var keys = Object.keys(obj[0]);
        let objsKeys: ColumnMeta[] = []
        keys.forEach((e) => {
            objsKeys.push({ field: e, header: e })
        })
        setcColumnsJson(objsKeys)
        setDataJson(obj)
        console.log("Passei por aqui")
    }, []);

    useEffect(() => Streamlit.setFrameHeight())

    const template = (product: any, field: string) => {
        return <div className={field === "code" ? 'font-bold w-11rem' : ""}>{product[field]}</div>
    };

    const dynamicColumns = columnsJson.map((col, i) => {
        return <Column body={(e) => template(e, col.field)} headerClassName='' sortable frozen={i === 0} key={col.field} columnKey={col.field} field={col.field} header={col.header} />;
    });

    return (
        <>
            <div className="card">
                <DataTable
                    paginator 
                    rows={100} 
                    rowsPerPageOptions={[25, 50, 75, 100]}
                    size='small'
                    stripedRows
                    showGridlines
                    columnResizeMode='expand'
                    resizableColumns
                    scrollHeight='600px'
                    scrollable
                    value={dataJson}
                    reorderableColumns
                    tableStyle={{ minWidth: '50rem' }}>
                    {dynamicColumns}
                </DataTable>
            </div>
        </>
    );
}


export default withStreamlitConnection(ReorderDemo)
