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
    const [products, setProducts] = useState<Product[]>([]);
    const columns: ColumnMeta[] = [
        { field: 'code', header: 'Code' },
        { field: 'name', header: 'Name' },
        { field: 'category', header: 'Category' },
        { field: 'quantity', header: 'Quantity' },
        { field: 'price', header: 'price' },
        { field: 'inventoryStatus', header: 'inventoryStatus' },
        { field: 'rating', header: 'rating' },
        { field: 'image', header: 'image' },
        { field: 'description', header: 'description' },
        { field: 'lastname', header: 'lastname' },
        { field: 'qdtecotas', header: 'Quantidade Cotas' },
        { field: 'Iguacu', header: 'Iguacu' },
        { field: 'Cidade', header: 'Cidade' },
    ];

    useEffect(() => {
        ProductService.getProducts().then((data) => setProducts(data));
        console.log(JSON.parse(args.html))
    }, []);

    useEffect(() => Streamlit.setFrameHeight())

    const template = (product: Product, field: string) => {
        return <div className={field === "code" ? 'font-bold w-11rem' : ""}>{product[field]}</div>
    };

    const dynamicColumns = columns.map((col, i) => {
        return <Column body={(e) => template(e, col.field)} headerClassName='' sortable frozen={i === 0} key={col.field} columnKey={col.field} field={col.field} header={col.header} />;
    });

    return (
        <>
            <div className="card">
                <DataTable
                    size='small'
                    stripedRows
                    showGridlines
                    columnResizeMode='expand'
                    resizableColumns
                    scrollHeight='600px'
                    scrollable
                    value={products}
                    reorderableColumns
                    tableStyle={{ minWidth: '50rem' }}>
                    {dynamicColumns}
                </DataTable>
            </div>
        </>
    );
}


export default withStreamlitConnection(ReorderDemo)
